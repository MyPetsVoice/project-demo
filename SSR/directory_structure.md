# Flask 프로젝트 구조 및 공통 컴포넌트 관리 방안

## 1. 권장 프로젝트 구조

```
mypets_voice/
├── app.py                          # Flask 메인 애플리케이션
├── requirements.txt                # Python 패키지 의존성
├── config.py                      # 설정 파일
├── static/
│   ├── css/
│   │   ├── base.css              # 공통 스타일
│   │   ├── components.css        # 컴포넌트별 스타일
│   │   ├── navbar.css           # 네비게이션 스타일
│   │   ├── footer.css           # 푸터 스타일
│   │   ├── chat.css             # 채팅 페이지 스타일
│   │   ├── diary.css            # 일기 페이지 스타일
│   │   ├── community.css        # 커뮤니티 페이지 스타일
│   │   ├── place.css            # 플레이스 페이지 스타일
│   │   ├── tourspot.css         # 투어스팟 페이지 스타일
│   │   ├── dailycare.css        # 데일리케어 페이지 스타일
│   │   └── mypage.css           # 마이페이지 스타일
│   ├── js/
│   │   ├── common.js            # 공통 JavaScript
│   │   ├── navbar.js            # 네비게이션 기능
│   │   ├── auth.js              # 인증 관련 기능
│   │   ├── chat.js              # 채팅 기능
│   │   ├── diary.js             # 일기 기능
│   │   ├── community.js         # 커뮤니티 기능
│   │   ├── place.js             # 플레이스 기능
│   │   ├── tourspot.js          # 투어스팟 기능
│   │   ├── dailycare.js         # 데일리케어 기능
│   │   └── mypage.js            # 마이페이지 기능
│   └── images/                  # 이미지 파일들
├── templates/
│   ├── base.html               # 기본 레이아웃 템플릿
│   ├── components/             # 재사용 가능한 컴포넌트들
│   │   ├── navbar.html
│   │   ├── footer.html
│   │   ├── pet_card.html
│   │   └── modal.html
│   ├── auth/                   # 인증 관련 템플릿
│   │   ├── login.html
│   │   ├── signup.html
│   │   └── profile.html
│   ├── chat/
│   │   └── index.html
│   ├── diary/
│   │   ├── index.html
│   │   ├── create.html
│   │   └── detail.html
│   ├── community/
│   │   ├── index.html
│   │   ├── create.html
│   │   └── detail.html
│   ├── place/
│   │   └── index.html
│   ├── tourspot/
│   │   └── index.html
│   ├── dailycare/
│   │   ├── index.html
│   │   ├── health.html
│   │   └── routine.html
│   └── mypage/
│       └── index.html
├── models/                     # 데이터베이스 모델
│   ├── __init__.py
│   ├── user.py
│   ├── pet.py
│   ├── diary.py
│   └── community.py
├── routes/                     # 라우트 파일들
│   ├── __init__.py
│   ├── auth.py
│   ├── chat.py
│   ├── diary.py
│   ├── community.py
│   ├── place.py
│   ├── tourspot.py
│   ├── dailycare.py
│   └── mypage.py
└── utils/                     # 유틸리티 함수들
    ├── __init__.py
    ├── helpers.py
    └── decorators.py
```

## 2. 기본 템플릿 구조 (base.html)

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}MyPet's Voice{% endblock %}</title>
    
    <!-- 공통 CSS -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/base.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/components.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/navbar.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/footer.css') }}">
    
    <!-- 페이지별 CSS -->
    {% block styles %}{% endblock %}
    
    <!-- 페이지별 메타 태그 -->
    {% block meta %}{% endblock %}
</head>
<body>
    <!-- 네비게이션 include -->
    {% include 'components/navbar.html' %}
    
    <!-- 메인 컨텐츠 영역 -->
    <main class="main-container">
        {% block content %}{% endblock %}
    </main>
    
    <!-- 푸터 include -->
    {% include 'components/footer.html' %}
    
    <!-- 공통 JavaScript -->
    <script src="{{ url_for('static', filename='js/common.js') }}"></script>
    <script src="{{ url_for('static', filename='js/navbar.js') }}"></script>
    <script src="{{ url_for('static', filename='js/auth.js') }}"></script>
    
    <!-- 페이지별 JavaScript -->
    {% block scripts %}{% endblock %}
</body>
</html>
```

## 3. 네비게이션 컴포넌트 (components/navbar.html)

```html
<nav class="navbar">
    <div class="nav-container">
        <a href="{{ url_for('main.index') }}" class="nav-link">
            <div class="nav-logo">
                <i class="fas fa-paw"></i>
                <span>MyPet's Voice</span>
            </div>
        </a>
        
        <button class="mobile-menu-toggle" id="mobile-menu-toggle">
            <i class="fas fa-bars"></i>
        </button>
        
        <div class="nav-menu" id="nav-menu">
            <a href="{{ url_for('diary.index') }}" 
               class="nav-link {% if request.endpoint and 'diary' in request.endpoint %}active{% endif %}">
                너의 일기장
            </a>
            <a href="{{ url_for('community.index') }}" 
               class="nav-link {% if request.endpoint and 'community' in request.endpoint %}active{% endif %}">
                커뮤니티
            </a>
            <a href="{{ url_for('place.index') }}" 
               class="nav-link {% if request.endpoint and 'place' in request.endpoint %}active{% endif %}">
                플레이스
            </a>
            <a href="{{ url_for('tourspot.index') }}" 
               class="nav-link {% if request.endpoint and 'tourspot' in request.endpoint %}active{% endif %}">
                투어스팟
            </a>
            <a href="{{ url_for('dailycare.index') }}" 
               class="nav-link {% if request.endpoint and 'dailycare' in request.endpoint %}active{% endif %}">
                데일리케어
            </a>
            <a href="{{ url_for('mypage.index') }}" 
               class="nav-link {% if request.endpoint and 'mypage' in request.endpoint %}active{% endif %}">
                마이페이지
            </a>
        </div>

        <div class="nav-user">
            {% if session.user_id %}
                <div class="user-menu">
                    <button class="user-avatar" id="user-menu-btn">
                        <img src="{{ session.user_avatar or url_for('static', filename='images/default-avatar.png') }}" 
                             alt="프로필">
                    </button>
                    <div class="user-dropdown" id="user-dropdown">
                        <a href="{{ url_for('mypage.index') }}">마이페이지</a>
                        <a href="{{ url_for('auth.logout') }}">로그아웃</a>
                    </div>
                </div>
            {% else %}
                <button class="btn btn-primary" id="login-btn">
                    <i class="fas fa-sign-in-alt"></i> 로그인
                </button>
                <button class="btn btn-outline" id="signup-btn">
                    회원가입
                </button>
            {% endif %}
        </div>
    </div>
</nav>
```

## 4. 푸터 컴포넌트 (components/footer.html)

```html
<footer class="footer">
    <div class="footer-container">
        <div class="footer-content">
            <div class="footer-section">
                <div class="footer-logo">
                    <i class="fas fa-paw"></i>
                    <span>MyPet's Voice</span>
                </div>
                <p class="footer-description">
                    반려동물과의 특별한 소통을 위한 AI 플랫폼
                </p>
                <div class="footer-social">
                    <a href="#" class="social-link" data-platform="instagram">
                        <i class="fab fa-instagram"></i>
                    </a>
                    <a href="#" class="social-link" data-platform="facebook">
                        <i class="fab fa-facebook"></i>
                    </a>
                    <a href="#" class="social-link" data-platform="twitter">
                        <i class="fab fa-twitter"></i>
                    </a>
                    <a href="#" class="social-link" data-platform="youtube">
                        <i class="fab fa-youtube"></i>
                    </a>
                </div>
            </div>

            <div class="footer-section">
                <h4>서비스</h4>
                <ul>
                    <li><a href="{{ url_for('chat.index') }}">AI 채팅</a></li>
                    <li><a href="{{ url_for('diary.index') }}">반려동물 일기</a></li>
                    <li><a href="{{ url_for('community.index') }}">커뮤니티</a></li>
                    <li><a href="{{ url_for('place.index') }}">플레이스</a></li>
                </ul>
            </div>

            <div class="footer-section">
                <h4>고객지원</h4>
                <ul>
                    <li><a href="#" class="footer-link" data-action="notice">공지사항</a></li>
                    <li><a href="#" class="footer-link" data-action="faq">자주 묻는 질문</a></li>
                    <li><a href="#" class="footer-link" data-action="contact">문의하기</a></li>
                    <li><a href="#" class="footer-link" data-action="guide">이용가이드</a></li>
                </ul>
            </div>

            <div class="footer-section">
                <h4>정보</h4>
                <ul>
                    <li><a href="#" class="footer-link" data-action="about">회사소개</a></li>
                    <li><a href="#" class="footer-link" data-action="terms">이용약관</a></li>
                    <li><a href="#" class="footer-link" data-action="privacy">개인정보처리방침</a></li>
                    <li><a href="#" class="footer-link" data-action="business">사업자정보</a></li>
                </ul>
            </div>
        </div>

        <div class="footer-bottom">
            <div class="footer-copyright">
                <p>&copy; 2025 MyPet's Voice. All rights reserved.</p>
            </div>
            <div class="footer-contact">
                <p>문의: contact@mypetsvoice.com | 대표번호: 02-1234-5678</p>
            </div>
        </div>
    </div>
</footer>
```

## 5. 개별 페이지 예시 (diary/index.html)

```html
{% extends "base.html" %}

{% block title %}너의 일기장 - MyPet's Voice{% endblock %}

{% block styles %}
<link rel="stylesheet" href="{{ url_for('static', filename='css/diary.css') }}">
{% endblock %}

{% block content %}
<div class="diary-container">
    <div class="diary-header">
        <h2>반려동물 일기</h2>
        <div class="diary-actions">
            <button class="btn btn-primary" id="create-diary-btn">
                <i class="fas fa-plus"></i> 일기 쓰기
            </button>
        </div>
    </div>

    <div class="diary-filters">
        <select id="diary-pet-filter">
            <option value="">모든 반려동물</option>
            {% for pet in user_pets %}
            <option value="{{ pet.id }}">{{ pet.name }}</option>
            {% endfor %}
        </select>
        <div class="view-toggle">
            <button class="view-btn active" data-view="my">내 일기</button>
            <button class="view-btn" data-view="public">공개 일기</button>
        </div>
    </div>

    <div class="diary-grid" id="diary-grid">
        <!-- 일기 카드들이 JavaScript로 동적 로드됩니다 -->
    </div>
</div>
{% endblock %}

{% block scripts %}
<script src="{{ url_for('static', filename='js/diary.js') }}"></script>
{% endblock %}
```

## 6. 공통 JavaScript (static/js/common.js)

```javascript
// 공통 유틸리티 함수들
class CommonUtils {
    static showLoading() {
        // 로딩 표시
    }
    
    static hideLoading() {
        // 로딩 숨김
    }
    
    static showToast(message, type = 'info') {
        // 토스트 메시지 표시
    }
    
    static formatDate(date) {
        // 날짜 포맷팅
    }
    
    static async apiCall(url, options = {}) {
        // API 호출 공통 함수
        try {
            this.showLoading();
            const response = await fetch(url, {
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': this.getCSRFToken(),
                    ...options.headers
                },
                ...options
            });
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            return await response.json();
        } catch (error) {
            this.showToast('오류가 발생했습니다.', 'error');
            throw error;
        } finally {
            this.hideLoading();
        }
    }
    
    static getCSRFToken() {
        return document.querySelector('meta[name=csrf-token]').getAttribute('content');
    }
}

// 전역 변수로 설정
window.CommonUtils = CommonUtils;
```

## 7. 네비게이션 JavaScript (static/js/navbar.js)

```javascript
class NavbarManager {
    constructor() {
        this.init();
    }
    
    init() {
        this.setupMobileMenu();
        this.setupUserMenu();
        this.setupAuthButtons();
    }
    
    setupMobileMenu() {
        const mobileToggle = document.getElementById('mobile-menu-toggle');
        const navMenu = document.getElementById('nav-menu');
        
        if (mobileToggle) {
            mobileToggle.addEventListener('click', () => {
                navMenu.classList.toggle('active');
            });
        }
    }
    
    setupUserMenu() {
        const userMenuBtn = document.getElementById('user-menu-btn');
        const userDropdown = document.getElementById('user-dropdown');
        
        if (userMenuBtn && userDropdown) {
            userMenuBtn.addEventListener('click', (e) => {
                e.stopPropagation();
                userDropdown.classList.toggle('active');
            });
            
            document.addEventListener('click', () => {
                userDropdown.classList.remove('active');
            });
        }
    }
    
    setupAuthButtons() {
        const loginBtn = document.getElementById('login-btn');
        const signupBtn = document.getElementById('signup-btn');
        
        if (loginBtn) {
            loginBtn.addEventListener('click', () => {
                window.location.href = '/auth/login';
            });
        }
        
        if (signupBtn) {
            signupBtn.addEventListener('click', () => {
                window.location.href = '/auth/signup';
            });
        }
    }
}

// DOM 로드 완료 시 초기화
document.addEventListener('DOMContentLoaded', () => {
    new NavbarManager();
});
```

## 8. 메인 Flask 애플리케이션 (app.py)

```python
from flask import Flask, render_template
from routes import auth, chat, diary, community, place, tourspot, dailycare, mypage

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    # 블루프린트 등록
    app.register_blueprint(auth.bp, url_prefix='/auth')
    app.register_blueprint(chat.bp, url_prefix='/chat')
    app.register_blueprint(diary.bp, url_prefix='/diary')
    app.register_blueprint(community.bp, url_prefix='/community')
    app.register_blueprint(place.bp, url_prefix='/place')
    app.register_blueprint(tourspot.bp, url_prefix='/tourspot')
    app.register_blueprint(dailycare.bp, url_prefix='/dailycare')
    app.register_blueprint(mypage.bp, url_prefix='/mypage')
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
```

## 9. 개발자별 작업 가이드

### 각 개발자가 해야 할 일:

1. **자신의 라우트 파일 작성** (routes/모듈명.py)
2. **템플릿 작성** (templates/모듈명/)
3. **CSS 작성** (static/css/모듈명.css)
4. **JavaScript 작성** (static/js/모듈명.js)

### 공통 컴포넌트 수정이 필요한 경우:
- base.html, navbar.html, footer.html 수정은 팀 전체 협의 후 진행
- 공통 CSS/JS 수정 시 다른 개발자들에게 알림

이 구조의 장점:
1. **모듈화**: 각 기능별로 파일이 분리되어 있어 충돌 최소화
2. **재사용성**: 공통 컴포넌트를 여러 페이지에서 재사용
3. **유지보수성**: 공통 부분 수정 시 모든 페이지에 자동 반영
4. **Flask 친화적**: Flask의 템플릿 상속과 블루프린트 활용
5. **확장성**: 새로운 기능 추가 시 기존 구조 유지하며 확장 가능