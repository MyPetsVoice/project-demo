#!/usr/bin/env python3
"""
PetCare 디버그 서버
상세한 로그와 함께 문제를 진단합니다.
"""

import os
import sys
import traceback
from flask import Flask

# 로깅 설정
import logging
logging.basicConfig(level=logging.DEBUG)

print("🔧 PetCare 디버그 모드 시작...")

# 현재 디렉토리 확인
print(f"📁 현재 작업 디렉토리: {os.getcwd()}")

# 환경변수 설정
os.environ['FLASK_ENV'] = 'development'
os.environ['FLASK_DEBUG'] = '1'

try:
    print("📦 모듈 import 시작...")
    
    # 단계별 import
    print("  1. Flask 기본 모듈...")
    from flask import Flask, render_template
    
    print("  2. models 모듈...")
    from models import db, User
    
    print("  3. app 모듈...")
    # app 모듈을 직접 import 하지 말고 필요한 부분만 복사
    
    # 기본 Flask 앱 생성
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'debug-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///debug.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # 데이터베이스 초기화
    db.init_app(app)
    
    print("✅ 모든 모듈 import 성공!")
    
    @app.route('/')
    def index():
        try:
            return render_template('index.html')
        except Exception as e:
            error_info = traceback.format_exc()
            return f'''
            <h1>템플릿 오류 상세 정보</h1>
            <h3>오류:</h3>
            <pre>{str(e)}</pre>
            <h3>상세 스택 트레이스:</h3>
            <pre>{error_info}</pre>
            '''
    
    @app.route('/debug')
    def debug_info():
        return f'''
        <h1>🔧 PetCare 디버그 정보</h1>
        <h2>📊 시스템 정보</h2>
        <ul>
            <li><strong>Python 버전:</strong> {sys.version}</li>
            <li><strong>Flask 앱:</strong> {app}</li>
            <li><strong>작업 디렉토리:</strong> {os.getcwd()}</li>
            <li><strong>템플릿 폴더:</strong> {app.template_folder}</li>
            <li><strong>정적 파일 폴더:</strong> {app.static_folder}</li>
        </ul>
        
        <h2>📁 파일 시스템</h2>
        <ul>
            <li>templates 폴더 존재: {os.path.exists('templates')}</li>
            <li>static 폴더 존재: {os.path.exists('static')}</li>
            <li>index.html 존재: {os.path.exists('templates/index.html')}</li>
        </ul>
        
        <h2>🔗 테스트 링크</h2>
        <ul>
            <li><a href="/">메인 페이지 (index.html)</a></li>
            <li><a href="/simple">간단 페이지</a></li>
        </ul>
        '''
    
    @app.route('/simple')
    def simple():
        return '''
        <h1>✅ 간단 페이지 작동!</h1>
        <p>이 페이지가 보인다면 Flask 라우팅은 정상입니다.</p>
        <p><a href="/debug">디버그 정보로 돌아가기</a></p>
        '''
    
    print("\n🚀 디버그 서버 시작...")
    print("📍 다음 URL들을 차례로 확인해보세요:")
    print("   http://localhost:5000/debug   (디버그 정보)")
    print("   http://localhost:5000/simple  (간단 테스트)")
    print("   http://localhost:5000         (메인 페이지)")
    
    # 데이터베이스 초기화
    with app.app_context():
        db.create_all()
        print("✅ 데이터베이스 초기화 완료")
    
    # 서버 실행
    app.run(debug=True, host='127.0.0.1', port=5000, use_reloader=False)

except Exception as e:
    print(f"\n❌ 오류 발생:")
    print(f"   {str(e)}")
    print(f"\n📋 상세 오류 정보:")
    traceback.print_exc()
    
    print(f"\n🔧 가능한 해결 방법:")
    print(f"   1. 의존성 재설치: pip install -r requirements.txt")
    print(f"   2. 다른 터미널에서 실행")
    print(f"   3. 포트 변경하여 재시도")
    
    sys.exit(1)