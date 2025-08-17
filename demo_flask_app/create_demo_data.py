#!/usr/bin/env python3
"""
데모 데이터 생성 스크립트
"""

from models import db, User, Pet, Diary, CommunityPost
from werkzeug.security import generate_password_hash
from datetime import datetime

def create_demo_user():
    """데모 사용자와 데이터 생성"""
    
    # 기존 데모 사용자 삭제 (있다면)
    existing_user = User.query.filter_by(username='demo').first()
    if existing_user:
        db.session.delete(existing_user)
        print("기존 데모 사용자 삭제됨")
    
    # 새 데모 사용자 생성
    demo_user = User(
        username='demo',
        email='demo@petcare.com',
        nickname='데모사용자',
        password_hash=generate_password_hash('demo1234!')  # 간단한 비밀번호
    )
    
    db.session.add(demo_user)
    db.session.commit()
    print(f"✅ 데모 사용자 생성완료: {demo_user.username}")
    
    # 테스트 사용자도 생성
    test_user = User(
        username='test',
        email='test@test.com',
        nickname='테스트유저',
        password_hash=generate_password_hash('test1234!')
    )
    
    db.session.add(test_user)
    db.session.commit()
    print(f"✅ 테스트 사용자 생성완료: {test_user.username}")
    
    return demo_user, test_user

def main():
    """메인 실행 함수"""
    from app import app
    
    with app.app_context():
        # 데이터베이스 초기화
        db.create_all()
        print("🗄️ 데이터베이스 테이블 생성 완료")
        
        # 데모 사용자 생성
        demo_user, test_user = create_demo_user()
        
        print("\n🎯 데모 계정 정보:")
        print("="*40)
        print("계정 1:")
        print(f"  아이디: demo")
        print(f"  비밀번호: demo1234!")
        print(f"  닉네임: {demo_user.nickname}")
        print()
        print("계정 2:")
        print(f"  아이디: test")
        print(f"  비밀번호: test1234!")
        print(f"  닉네임: {test_user.nickname}")
        print("="*40)
        print("\n🚀 이제 서버를 시작하고 위 계정으로 로그인해보세요!")

if __name__ == '__main__':
    main()