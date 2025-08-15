#!/usr/bin/env python3
"""
PetCare 간단 시작 스크립트
문제 진단 및 안전한 시작
"""

import os
import sys
from flask import Flask, render_template

# 환경변수 설정
os.environ['FLASK_ENV'] = 'development'

print("🔍 PetCare 서버 시작 진단...")

# 1. 기본 Flask 앱 생성
app = Flask(__name__)
app.config['SECRET_KEY'] = 'test-secret-key'

# 2. 기본 라우트 추가
@app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        return f'''
        <!DOCTYPE html>
        <html>
        <head>
            <title>PetCare - 템플릿 오류</title>
            <meta charset="UTF-8">
        </head>
        <body>
            <h1>⚠️ 템플릿 로딩 오류</h1>
            <p>오류: {e}</p>
            <p>templates/index.html 파일을 확인해주세요.</p>
            <hr>
            <h2>🔧 임시 메인 페이지</h2>
            <p>PetCare 서비스가 곧 시작됩니다!</p>
            <ul>
                <li><a href="/test">테스트 페이지</a></li>
                <li><a href="/health">서버 상태</a></li>
            </ul>
        </body>
        </html>
        '''

@app.route('/test')
def test():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>PetCare 테스트</title>
        <meta charset="UTF-8">
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            .success { color: green; }
            .info { color: blue; }
        </style>
    </head>
    <body>
        <h1 class="success">✅ PetCare 서버 정상 작동!</h1>
        
        <h2>📊 시스템 정보</h2>
        <ul>
            <li><strong>Flask:</strong> 정상 작동</li>
            <li><strong>Port:</strong> 5000</li>
            <li><strong>Host:</strong> localhost (127.0.0.1)</li>
            <li><strong>Debug:</strong> True</li>
        </ul>
        
        <h2>🔗 테스트 링크</h2>
        <ul>
            <li><a href="/">메인 페이지</a></li>
            <li><a href="/health">서버 상태</a></li>
        </ul>
        
        <h2>📝 다음 단계</h2>
        <ol>
            <li>이 페이지가 정상적으로 보인다면 서버는 정상입니다</li>
            <li>메인 페이지에서 템플릿 오류가 있다면 templates 폴더를 확인하세요</li>
            <li>모든 게 정상이면 풀 버전을 실행하세요: <code>python app.py</code></li>
        </ol>
    </body>
    </html>
    '''

@app.route('/health')
def health():
    return {
        'status': 'OK', 
        'message': 'PetCare server is running',
        'port': 5000,
        'debug': True
    }

# 3. 파일 존재 확인
def check_files():
    print("📁 필수 파일 확인 중...")
    
    required_files = [
        'templates/index.html',
        'templates/base.html', 
        'static/css/style.css',
        'static/js/main.js'
    ]
    
    for file_path in required_files:
        full_path = os.path.join(os.getcwd(), file_path)
        if os.path.exists(full_path):
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path} - 파일이 없습니다!")

if __name__ == '__main__':
    check_files()
    
    print("\n🚀 PetCare 간단 서버 시작...")
    print("📍 브라우저에서 다음 URL들을 확인해보세요:")
    print("   http://localhost:5000        (메인 페이지)")
    print("   http://localhost:5000/test   (테스트 페이지)")
    print("   http://localhost:5000/health (서버 상태)")
    print("🛑 종료하려면 Ctrl+C를 누르세요\n")
    
    try:
        # localhost로 제한하여 방화벽 문제 방지
        app.run(debug=True, host='127.0.0.1', port=5000, threaded=True)
    except OSError as e:
        if "Address already in use" in str(e):
            print("❌ 포트 5000이 이미 사용 중입니다!")
            print("🔧 다른 포트로 시도합니다...")
            app.run(debug=True, host='127.0.0.1', port=5002, threaded=True)
        else:
            print(f"❌ 서버 시작 오류: {e}")
    except Exception as e:
        print(f"❌ 예상치 못한 오류: {e}")
        sys.exit(1)