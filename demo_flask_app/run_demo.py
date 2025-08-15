#!/usr/bin/env python3
"""
PetCare 데모 서버 실행 스크립트

사용법:
    python run_demo.py

주요 기능:
- 데이터베이스 자동 초기화
- 샘플 데이터 생성
- 개발 서버 실행
"""

import os
import sys
from datetime import datetime, date
from werkzeug.security import generate_password_hash

# Flask 앱을 import하기 전에 환경변수 설정
os.environ['FLASK_ENV'] = 'development'

try:
    # 먼저 models에서 db를 import한 다음 app import
    from models import User, Pet, Diary, CommunityPost, HealthRecord, CareRoutine, TravelDestination, Place, db
    from app import app
except ImportError as e:
    print(f"❌ 모듈 import 실패: {e}")
    print("pip install -r requirements.txt 명령어로 의존성을 설치해주세요.")
    sys.exit(1)

def create_sample_data():
    """샘플 데이터 생성"""
    print("📝 샘플 데이터 생성 중...")
    
    try:
        # 샘플 사용자 생성
        if not User.query.filter_by(username='demo').first():
            demo_user = User(
                username='demo',
                email='demo@petcare.com',
                nickname='데모사용자',
                password_hash=generate_password_hash('demo1234!')
            )
            db.session.add(demo_user)
            db.session.commit()
            
            # 샘플 반려동물 생성
            demo_pet = Pet(
                name='멍멍이',
                species='강아지',
                breed='골든 리트리버',
                gender='수컷',
                is_neutered=True,
                personality='활발하고 친근한 성격',
                speaking_style='귀엽고 애교 많은 말투',
                user_nickname='주인님',
                likes='산책, 간식, 공놀이',
                dislikes='목욕, 큰 소리',
                habits='아침마다 주인을 깨우는 습관이 있음',
                user_id=demo_user.id
            )
            db.session.add(demo_pet)
            
            demo_cat = Pet(
                name='야옹이',
                species='고양이',
                breed='페르시안',
                gender='암컷',
                is_neutered=True,
                personality='조용하고 우아한 성격',
                speaking_style='점잖고 품위있는 말투',
                user_nickname='집사님',
                likes='햇볕, 털실, 캣타워',
                dislikes='물, 시끄러운 소리',
                habits='높은 곳에 올라가는 것을 좋아함',
                user_id=demo_user.id
            )
            db.session.add(demo_cat)
            db.session.commit()
            
            # 샘플 일기 생성
            sample_diary = Diary(
                title='오늘은 공원에서 신나게 놀았어요!',
                content='''오늘은 정말 신나는 하루였어! 주인님이 나를 데리고 큰 공원에 갔거든. 🐕
                
넓은 잔디밭을 뛰어다니니까 정말 기분이 좋았어! 다른 강아지 친구들도 많이 만났고, 특히 같은 골든 리트리버 친구와 함께 공놀이를 했지 뭐야! 

주인님이 새로운 간식도 준비해오셨어. 내가 제일 좋아하는 치킨 간식이었거든! 맛있게 먹고 나서 더욱 힘이 났어.

집에 돌아와서는 피곤해서 바로 잠들었지만, 오늘만큼 행복한 날은 없었던 것 같아. 내일도 또 나가서 놀 수 있을까? 🎾

주인님, 오늘 정말 고마웠어! 사랑해! 💕''',
                weather='맑음',
                pet_id=demo_pet.id,
                is_public=True,
                likes=15
            )
            db.session.add(sample_diary)
            
            # 샘플 커뮤니티 게시글 생성
            sample_post = CommunityPost(
                title='강아지 산책 시 주의사항 공유드려요',
                content='''안녕하세요! 골든 리트리버 멍멍이를 키우고 있는 반려인입니다.

오늘은 강아지 산책할 때 주의해야 할 점들을 공유하고 싶어요.

1. 🌡️ 날씨 확인하기
- 너무 더운 날에는 아스팔트가 뜨거워져서 발가락이 다칠 수 있어요
- 손등으로 바닥을 5초간 대보고 뜨거우면 산책을 피해주세요

2. 🚗 교통안전
- 반드시 목줄을 착용하고, 짧게 잡아주세요
- 도로변에서는 항상 주의를 기울여주세요

3. 💧 물 준비
- 특히 여름철에는 중간중간 물을 마실 수 있도록 준비해주세요

4. 🐕 다른 강아지와의 만남
- 상대방 반려인의 동의 없이는 접촉을 피해주세요
- 우리 아이의 성격도 고려해주세요

모두 안전하고 즐거운 산책하세요! 😊''',
                tag='꿀팁',
                user_id=demo_user.id,
                likes=23,
                views=156
            )
            db.session.add(sample_post)
            
            # 샘플 건강 기록 생성
            health_record = HealthRecord(
                record_type='예방접종',
                title='종합백신 접종',
                description='DHPPL 5차 종합백신 접종 완료',
                record_date=date.today(),
                pet_id=demo_pet.id
            )
            db.session.add(health_record)
            
            # 샘플 케어 루틴 생성
            care_routine = CareRoutine(
                routine_type='약 복용',
                title='심장사상충 예방약',
                description='매월 15일 심장사상충 예방약 복용',
                frequency='매월',
                pet_id=demo_pet.id
            )
            db.session.add(care_routine)
            
            # 샘플 여행지 정보 생성
            travel_destination = TravelDestination(
                name='강아지와 함께하는 펜션',
                location='강원도 춘천시',
                description='넓은 마당과 산책로가 있는 반려동물 전용 펜션입니다.',
                pet_policies='소형견/대형견 모두 입실 가능, 추가 요금 없음',
                facilities='전용 마당, 산책로, 목욕시설, 사료/물그릇 제공',
                activities='자유 산책, 마당 놀이, 주변 산책로 이용 가능'
            )
            db.session.add(travel_destination)
            
            # 샘플 장소 정보 생성
            sample_place = Place(
                name='행복한 동물병원',
                address='서울시 강남구 테헤란로 123',
                category='병원',
                phone='02-1234-5678',
                description='친절한 진료와 합리적인 가격으로 유명한 동물병원입니다.',
                pet_friendly=True
            )
            db.session.add(sample_place)
            
            db.session.commit()
            print("✅ 샘플 데이터 생성 완료!")
            
    except Exception as e:
        print(f"❌ 샘플 데이터 생성 실패: {e}")
        db.session.rollback()

def check_dependencies():
    """필수 의존성 확인"""
    print("🔍 의존성 확인 중...")
    
    required_packages = [
        'flask', 'flask_sqlalchemy', 'flask_login', 
        'werkzeug', 'openai', 'python-dotenv'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"❌ 누락된 패키지: {', '.join(missing_packages)}")
        print("다음 명령어로 설치해주세요: pip install -r requirements.txt")
        return False
    
    print("✅ 모든 의존성이 설치되어 있습니다.")
    return True

def check_env_file():
    """환경 파일 확인"""
    print("🔍 환경 설정 확인 중...")
    
    if not os.path.exists('.env'):
        print("⚠️  .env 파일이 없습니다. .env.example을 참고하여 생성해주세요.")
        print("OpenAI API 키가 없으면 AI 기능이 제한됩니다.")
    else:
        print("✅ 환경 설정 파일이 있습니다.")
    
    # OpenAI API 키 확인
    openai_key = os.getenv('OPENAI_API_KEY')
    if not openai_key or openai_key == 'your-openai-api-key-here':
        print("⚠️  OpenAI API 키가 설정되지 않았습니다.")
        print("AI 채팅 및 일기 기능을 사용하려면 .env 파일에 OPENAI_API_KEY를 설정해주세요.")
    else:
        print("✅ OpenAI API 키가 설정되어 있습니다.")

def main():
    """메인 실행 함수"""
    print("🐾 PetCare 데모 서버를 시작합니다...\n")
    
    # 의존성 확인
    if not check_dependencies():
        sys.exit(1)
    
    # 환경 설정 확인
    check_env_file()
    
    # 데이터베이스 초기화
    print("\n💾 데이터베이스 초기화 중...")
    try:
        with app.app_context():
            db.create_all()
            print("✅ 데이터베이스 초기화 완료!")
            
            # 샘플 데이터 생성
            create_sample_data()
            
    except Exception as e:
        print(f"❌ 데이터베이스 초기화 실패: {e}")
        sys.exit(1)
    
    # 서버 정보 출력
    print("\n" + "="*50)
    print("🚀 PetCare 데모 서버가 실행됩니다!")
    print("="*50)
    print(f"📍 URL: http://localhost:5000")
    print(f"🕐 시작 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("\n📋 데모 계정 정보:")
    print("   아이디: demo")
    print("   비밀번호: demo1234!")
    print("\n🔧 주요 기능:")
    print("   ✅ 회원가입/로그인")
    print("   ✅ 반려동물 등록 및 관리")
    print("   ✅ AI 채팅 (OpenAI API 키 필요)")
    print("   ✅ AI 일기 작성")
    print("   ✅ 커뮤니티")
    print("   ✅ 케어 관리")
    print("   ✅ 장소/여행지 정보")
    print("\n💡 팁:")
    print("   - OpenAI API 키를 설정하면 AI 기능을 체험할 수 있습니다")
    print("   - Ctrl+C로 서버를 종료할 수 있습니다")
    print("="*50)
    
    # Flask 서버 실행
    try:
        app.run(debug=True, host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("\n👋 서버를 종료합니다. 안녕히 가세요!")
    except Exception as e:
        print(f"\n❌ 서버 실행 중 오류 발생: {e}")

if __name__ == '__main__':
    main()