#!/usr/bin/env python3
"""
PetCare 빠른 시작 스크립트
문제 없이 서버를 시작할 수 있습니다.
"""

import os
import sys

# 환경변수 설정
os.environ['FLASK_ENV'] = 'development'

try:
    # 안전한 순서로 import
    from models import db
    from app import app
    
    print("🐾 PetCare 서버를 시작합니다...")
    
    # 데이터베이스 초기화
    with app.app_context():
        db.create_all()
        print("✅ 데이터베이스 초기화 완료")
    
    print("🚀 서버 실행 중...")
    print("📍 URL: http://localhost:5000")
    print("🔍 브라우저에서 위 URL로 접속하세요!")
    print("🛑 종료하려면 Ctrl+C를 누르세요")
    
    # Flask 서버 실행
    app.run(debug=True, host='0.0.0.0', port=5000)
    
except ImportError as e:
    print(f"❌ Import 오류: {e}")
    print("필요한 패키지를 설치하세요: pip install -r requirements.txt")
    sys.exit(1)
except Exception as e:
    print(f"❌ 서버 실행 오류: {e}")
    sys.exit(1)