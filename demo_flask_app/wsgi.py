#!/usr/bin/env python3
"""
WSGI 엔트리포인트
직접 app.py를 실행하는 대신 이 파일을 사용하세요.
"""

from app import app, db

if __name__ == '__main__':
    # 데이터베이스 테이블 생성
    with app.app_context():
        db.create_all()
        print("✅ 데이터베이스 테이블이 생성되었습니다.")
    
    print("🚀 PetCare 서버가 시작됩니다...")
    print("📍 URL: http://localhost:5000")
    
    # Flask 개발 서버 실행
    app.run(debug=True, host='0.0.0.0', port=5000)