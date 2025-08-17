#!/usr/bin/env python3
"""
최소 기능 서버 - 로그인/회원가입 테스트용
"""

import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

# 환경 설정
os.environ['FLASK_ENV'] = 'development'

try:
    from models import db, User
    
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'minimal-test-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///minimal_test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    @app.route('/')
    def index():
        return '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>PetCare 미니멀 테스트</title>
            <meta charset="UTF-8">
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; }
                .form-group { margin: 15px 0; }
                input[type="text"], input[type="email"], input[type="password"] {
                    width: 200px; padding: 8px; margin: 5px;
                }
                button { padding: 10px 20px; margin: 10px; }
                .success { color: green; }
                .error { color: red; }
            </style>
        </head>
        <body>
            <h1>🐾 PetCare 로그인/회원가입 테스트</h1>
            
            <div style="display: flex; gap: 50px;">
                <div>
                    <h2>📝 회원가입</h2>
                    <form id="registerForm">
                        <div class="form-group">
                            <label>아이디:</label><br>
                            <input type="text" id="reg_username" required>
                        </div>
                        <div class="form-group">
                            <label>이메일:</label><br>
                            <input type="email" id="reg_email" required>
                        </div>
                        <div class="form-group">
                            <label>닉네임:</label><br>
                            <input type="text" id="reg_nickname" required>
                        </div>
                        <div class="form-group">
                            <label>비밀번호:</label><br>
                            <input type="password" id="reg_password" required>
                        </div>
                        <div class="form-group">
                            <label>비밀번호 확인:</label><br>
                            <input type="password" id="reg_confirm_password" required>
                        </div>
                        <button type="submit">회원가입</button>
                    </form>
                </div>
                
                <div>
                    <h2>🔐 로그인</h2>
                    <form id="loginForm">
                        <div class="form-group">
                            <label>아이디:</label><br>
                            <input type="text" id="login_username" required>
                        </div>
                        <div class="form-group">
                            <label>비밀번호:</label><br>
                            <input type="password" id="login_password" required>
                        </div>
                        <button type="submit">로그인</button>
                    </form>
                    
                    <div style="margin-top: 20px; padding: 10px; background: #f0f0f0;">
                        <h4>🎯 테스트 계정</h4>
                        <p>아이디: demo<br>비밀번호: demo123</p>
                        <button onclick="fillDemo()">데모 계정 자동 입력</button>
                    </div>
                </div>
            </div>
            
            <div id="message" style="margin-top: 20px;"></div>
            
            <script>
                function showMessage(text, isError = false) {
                    const msg = document.getElementById('message');
                    msg.innerHTML = '<div class="' + (isError ? 'error' : 'success') + '">' + text + '</div>';
                }
                
                function fillDemo() {
                    document.getElementById('login_username').value = 'demo';
                    document.getElementById('login_password').value = 'demo123';
                }
                
                // 회원가입 폼
                document.getElementById('registerForm').addEventListener('submit', async function(e) {
                    e.preventDefault();
                    
                    const username = document.getElementById('reg_username').value.trim();
                    const email = document.getElementById('reg_email').value.trim();
                    const nickname = document.getElementById('reg_nickname').value.trim();
                    const password = document.getElementById('reg_password').value;
                    const confirmPassword = document.getElementById('reg_confirm_password').value;
                    
                    if (password !== confirmPassword) {
                        showMessage('비밀번호가 일치하지 않습니다.', true);
                        return;
                    }
                    
                    try {
                        const response = await fetch('/register', {
                            method: 'POST',
                            headers: {'Content-Type': 'application/json'},
                            body: JSON.stringify({username, email, nickname, password})
                        });
                        
                        const result = await response.json();
                        
                        if (response.ok) {
                            showMessage(result.message);
                            document.getElementById('registerForm').reset();
                        } else {
                            showMessage(result.error, true);
                        }
                    } catch (error) {
                        showMessage('회원가입 중 오류가 발생했습니다: ' + error.message, true);
                    }
                });
                
                // 로그인 폼
                document.getElementById('loginForm').addEventListener('submit', async function(e) {
                    e.preventDefault();
                    
                    const username = document.getElementById('login_username').value.trim();
                    const password = document.getElementById('login_password').value;
                    
                    try {
                        const response = await fetch('/login', {
                            method: 'POST',
                            headers: {'Content-Type': 'application/json'},
                            body: JSON.stringify({username, password})
                        });
                        
                        const result = await response.json();
                        
                        if (response.ok) {
                            showMessage(result.message);
                        } else {
                            showMessage(result.error, true);
                        }
                    } catch (error) {
                        showMessage('로그인 중 오류가 발생했습니다: ' + error.message, true);
                    }
                });
            </script>
        </body>
        </html>
        '''
    
    @app.route('/register', methods=['POST'])
    def register():
        try:
            data = request.get_json()
            username = data.get('username', '').strip()
            email = data.get('email', '').strip()
            nickname = data.get('nickname', '').strip()
            password = data.get('password', '')
            
            print(f"회원가입 시도: {username}, {email}, {nickname}")
            
            if not all([username, email, nickname, password]):
                return jsonify({'error': '모든 필드를 입력해주세요.'}), 400
            
            if User.query.filter_by(username=username).first():
                return jsonify({'error': '이미 존재하는 아이디입니다.'}), 400
            
            new_user = User(
                username=username,
                email=email,
                nickname=nickname,
                password_hash=generate_password_hash(password)
            )
            
            db.session.add(new_user)
            db.session.commit()
            
            print(f"사용자 생성 성공: {username}")
            return jsonify({'message': f'회원가입 완료! {nickname}님 환영합니다.'}), 200
            
        except Exception as e:
            print(f"회원가입 오류: {e}")
            db.session.rollback()
            return jsonify({'error': str(e)}), 500
    
    @app.route('/login', methods=['POST'])
    def login():
        try:
            data = request.get_json()
            username = data.get('username', '').strip()
            password = data.get('password', '')
            
            print(f"로그인 시도: {username}")
            
            user = User.query.filter_by(username=username).first()
            
            if not user:
                return jsonify({'error': '존재하지 않는 아이디입니다.'}), 400
            
            if not check_password_hash(user.password_hash, password):
                return jsonify({'error': '비밀번호가 틀렸습니다.'}), 400
            
            print(f"로그인 성공: {username}")
            return jsonify({'message': f'{user.nickname}님, 로그인 성공!'}), 200
            
        except Exception as e:
            print(f"로그인 오류: {e}")
            return jsonify({'error': str(e)}), 500
    
    if __name__ == '__main__':
        print("🧪 미니멀 서버 시작...")
        
        with app.app_context():
            db.create_all()
            
            # 데모 사용자 생성
            if not User.query.filter_by(username='demo').first():
                demo_user = User(
                    username='demo',
                    email='demo@test.com',
                    nickname='데모유저',
                    password_hash=generate_password_hash('demo123')
                )
                db.session.add(demo_user)
                db.session.commit()
                print("✅ 데모 계정 생성: demo / demo123")
        
        print("📍 브라우저에서 http://localhost:5003 접속")
        app.run(debug=True, host='127.0.0.1', port=5003)

except Exception as e:
    print(f"❌ 서버 시작 실패: {e}")
    import traceback
    traceback.print_exc()