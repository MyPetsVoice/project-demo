from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os
from datetime import datetime
import requests
import openai
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///petcare.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# 업로드 폴더 생성
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# 모델 정의 먼저 import
from models import db, User, Pet, Diary, DiaryLike, CommunityPost, Comment, PostLike, HealthRecord, CareRoutine, ChatLog, Place, PlaceReview, TravelDestination

# 데이터베이스 초기화
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# OpenAI API 설정
from openai import OpenAI
openai_client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
) if os.getenv('OPENAI_API_KEY') else None

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# 메인 페이지
@app.route('/')
def index():
    # 인기 일기와 커뮤니티 게시글 가져오기
    popular_diaries = Diary.query.filter_by(is_public=True).order_by(Diary.likes.desc()).limit(5).all()
    popular_posts = CommunityPost.query.order_by(CommunityPost.likes.desc()).limit(5).all()
    
    return render_template('index.html', 
                         popular_diaries=popular_diaries, 
                         popular_posts=popular_posts)

# 회원가입
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            data = request.get_json() if request.is_json else request.form
            
            username = data.get('username', '').strip()
            email = data.get('email', '').strip()
            nickname = data.get('nickname', '').strip()
            password = data.get('password', '')
            
            print(f"Registration attempt: {username}, {email}, {nickname}")  # 디버그용
            
            # 필수 필드 확인
            if not all([username, email, nickname, password]):
                return jsonify({'error': '모든 필드를 입력해주세요.'}), 400
            
            # 기본 유효성 검사
            if len(username) < 4 or len(username) > 20:
                return jsonify({'error': '아이디는 4-20자여야 합니다.'}), 400
                
            if len(password) < 6:
                return jsonify({'error': '비밀번호는 최소 6자 이상이어야 합니다.'}), 400
            
            # 중복 체크
            if User.query.filter_by(username=username).first():
                return jsonify({'error': '이미 존재하는 아이디입니다.'}), 400
            
            if User.query.filter_by(email=email).first():
                return jsonify({'error': '이미 존재하는 이메일입니다.'}), 400
            
            # 새 사용자 생성
            new_user = User(
                username=username,
                email=email,
                nickname=nickname,
                password_hash=generate_password_hash(password)
            )
            
            db.session.add(new_user)
            db.session.commit()
            
            print(f"User created successfully: {username}")  # 디버그용
            return jsonify({'message': '회원가입이 완료되었습니다.'}), 200
            
        except Exception as e:
            print(f"Registration error: {e}")  # 디버그용
            db.session.rollback()
            return jsonify({'error': f'회원가입 중 오류가 발생했습니다: {str(e)}'}), 500
    
    return render_template('register.html')

# 로그인
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            data = request.get_json() if request.is_json else request.form
            
            username = data.get('username', '').strip()
            password = data.get('password', '')
            
            print(f"Login attempt: {username}")  # 디버그용
            
            if not username or not password:
                return jsonify({'error': '아이디와 비밀번호를 모두 입력해주세요.'}), 400
            
            user = User.query.filter_by(username=username).first()
            print(f"User found: {user is not None}")  # 디버그용
            
            if user:
                print(f"Checking password for user: {username}")  # 디버그용
                if check_password_hash(user.password_hash, password):
                    login_user(user)
                    print(f"Login successful for user: {username}")  # 디버그용
                    return jsonify({'message': '로그인 성공', 'redirect': url_for('dashboard')}), 200
                else:
                    print(f"Password check failed for user: {username}")  # 디버그용
                    return jsonify({'error': '비밀번호가 잘못되었습니다.'}), 400
            else:
                print(f"User not found: {username}")  # 디버그용
                return jsonify({'error': '존재하지 않는 아이디입니다.'}), 400
                
        except Exception as e:
            print(f"Login error: {e}")  # 디버그용
            return jsonify({'error': f'로그인 중 오류가 발생했습니다: {str(e)}'}), 500
    
    return render_template('login.html')

# 로그아웃
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

# 대시보드
@app.route('/dashboard')
@login_required
def dashboard():
    user_pets = Pet.query.filter_by(user_id=current_user.id).all()
    recent_diaries = Diary.query.join(Pet).filter(Pet.user_id == current_user.id).order_by(Diary.created_at.desc()).limit(3).all()
    
    return render_template('dashboard.html', pets=user_pets, recent_diaries=recent_diaries)

# 반려동물 프로필 관리
@app.route('/pets')
@login_required
def pets():
    user_pets = Pet.query.filter_by(user_id=current_user.id).all()
    return render_template('pets.html', pets=user_pets)

@app.route('/pets/add', methods=['GET', 'POST'])
@login_required
def add_pet():
    if request.method == 'POST':
        data = request.get_json() if request.is_json else request.form
        
        new_pet = Pet(
            name=data.get('name'),
            species=data.get('species'),
            breed=data.get('breed'),
            gender=data.get('gender'),
            is_neutered=data.get('is_neutered') == 'true',
            personality=data.get('personality'),
            speaking_style=data.get('speaking_style'),
            user_nickname=data.get('user_nickname'),
            likes=data.get('likes'),
            dislikes=data.get('dislikes'),
            habits=data.get('habits'),
            user_id=current_user.id
        )
        
        db.session.add(new_pet)
        db.session.commit()
        
        return jsonify({'message': '반려동물이 등록되었습니다.', 'redirect': url_for('pets')}), 200
    
    return render_template('add_pet.html')

# AI 챗봇
@app.route('/chat/<int:pet_id>')
@login_required
def chat(pet_id):
    pet = Pet.query.filter_by(id=pet_id, user_id=current_user.id).first_or_404()
    return render_template('chat.html', pet=pet)

@app.route('/api/chat', methods=['POST'])
@login_required
def api_chat():
    data = request.get_json()
    pet_id = data.get('pet_id')
    message = data.get('message')
    
    pet = Pet.query.filter_by(id=pet_id, user_id=current_user.id).first_or_404()
    
    # AI 응답 생성
    try:
        if not openai_client:
            return jsonify({'error': 'OpenAI API 키가 설정되지 않았습니다. 관리자에게 문의하세요.'}), 500
            
        response = openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": f"""
                    당신은 {pet.name}이라는 이름의 {pet.species} {pet.breed}입니다.
                    성격: {pet.personality}
                    말투: {pet.speaking_style}
                    주인을 부르는 호칭: {pet.user_nickname or '주인'}
                    좋아하는 것: {pet.likes}
                    싫어하는 것: {pet.dislikes}
                    습관: {pet.habits}
                    
                    반려동물의 관점에서 주인과 대화하세요. 친근하고 애정어린 톤으로 대화하며, 
                    때로는 장난스럽고 귀여운 모습을 보여주세요.
                    """
                },
                {"role": "user", "content": message}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        ai_response = response.choices[0].message.content
        
        # 대화 기록 저장
        chat_log = ChatLog(
            pet_id=pet_id,
            user_message=message,
            ai_response=ai_response
        )
        db.session.add(chat_log)
        db.session.commit()
        
        return jsonify({'response': ai_response}), 200
        
    except Exception as e:
        return jsonify({'error': 'AI 응답 생성 중 오류가 발생했습니다.'}), 500

# 일기 작성
@app.route('/diary')
@login_required
def diary_list():
    user_pets = Pet.query.filter_by(user_id=current_user.id).all()
    return render_template('diary_list.html', pets=user_pets)

@app.route('/diary/<int:pet_id>')
@login_required
def pet_diary(pet_id):
    pet = Pet.query.filter_by(id=pet_id, user_id=current_user.id).first_or_404()
    diaries = Diary.query.filter_by(pet_id=pet_id).order_by(Diary.created_at.desc()).all()
    return render_template('pet_diary.html', pet=pet, diaries=diaries)

@app.route('/diary/write/<int:pet_id>', methods=['GET', 'POST'])
@login_required
def write_diary(pet_id):
    pet = Pet.query.filter_by(id=pet_id, user_id=current_user.id).first_or_404()
    
    if request.method == 'POST':
        data = request.get_json() if request.is_json else request.form
        
        title = data.get('title')
        content_summary = data.get('content_summary')
        weather = data.get('weather', '맑음')
        
        # AI로 일기 생성
        try:
            if not openai_client:
                return jsonify({'error': 'OpenAI API 키가 설정되지 않았습니다. 관리자에게 문의하세요.'}), 500
                
            response = openai_client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": f"""
                        당신은 {pet.name}이라는 {pet.species} {pet.breed}입니다.
                        오늘 있었던 일을 바탕으로 일기를 작성해주세요.
                        반려동물의 관점에서 하루를 돌아보며, 감정과 생각을 표현하세요.
                        귀엽고 따뜻한 문체로 작성해주세요.
                        """
                    },
                    {
                        "role": "user", 
                        "content": f"오늘 날씨: {weather}\n오늘 있었던 일: {content_summary}\n\n이 내용을 바탕으로 일기를 작성해주세요."
                    }
                ],
                max_tokens=800,
                temperature=0.8
            )
            
            ai_content = response.choices[0].message.content
            
            new_diary = Diary(
                title=title,
                content=ai_content,
                weather=weather,
                pet_id=pet_id,
                is_public=data.get('is_public') == 'true'
            )
            
            db.session.add(new_diary)
            db.session.commit()
            
            return jsonify({
                'message': '일기가 작성되었습니다.',
                'diary_content': ai_content,
                'redirect': url_for('pet_diary', pet_id=pet_id)
            }), 200
            
        except Exception as e:
            return jsonify({'error': '일기 생성 중 오류가 발생했습니다.'}), 500
    
    return render_template('write_diary.html', pet=pet)

# 커뮤니티
@app.route('/community')
def community():
    posts = CommunityPost.query.order_by(CommunityPost.created_at.desc()).all()
    return render_template('community.html', posts=posts)

@app.route('/community/write', methods=['GET', 'POST'])
@login_required
def write_post():
    if request.method == 'POST':
        data = request.get_json() if request.is_json else request.form
        
        new_post = CommunityPost(
            title=data.get('title'),
            content=data.get('content'),
            tag=data.get('tag'),
            user_id=current_user.id
        )
        
        db.session.add(new_post)
        db.session.commit()
        
        return jsonify({'message': '게시글이 작성되었습니다.', 'redirect': url_for('community')}), 200
    
    return render_template('write_post.html')

# 반려동물 케어
@app.route('/care')
@login_required
def care():
    user_pets = Pet.query.filter_by(user_id=current_user.id).all()
    return render_template('care.html', pets=user_pets)

@app.route('/care/<int:pet_id>')
@login_required
def pet_care(pet_id):
    pet = Pet.query.filter_by(id=pet_id, user_id=current_user.id).first_or_404()
    health_records = HealthRecord.query.filter_by(pet_id=pet_id).order_by(HealthRecord.created_at.desc()).all()
    care_routines = CareRoutine.query.filter_by(pet_id=pet_id).all()
    
    return render_template('pet_care.html', pet=pet, health_records=health_records, care_routines=care_routines)

# 지도 및 여행지 정보
@app.route('/places')
def places():
    return render_template('places.html')

@app.route('/travel')
def travel():
    return render_template('travel.html')

# 애플리케이션 팩토리 패턴을 위한 함수
def create_app():
    return app

if __name__ == '__main__':
    print("⚠️  직접 app.py를 실행하는 대신 다음 명령어를 사용하세요:")
    print("   python run_demo.py  (권장)")
    print("   또는")
    print("   python wsgi.py")
    print("\n계속 진행하려면 Enter를 누르세요...")
    input()
    
    try:
        with app.app_context():
            db.create_all()
            print("✅ 데이터베이스 초기화 완료")
    except Exception as e:
        print(f"❌ 데이터베이스 초기화 실패: {e}")
    
    app.run(debug=True, host='0.0.0.0', port=5000)