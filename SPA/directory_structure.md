# SPA 방식 프로젝트 구조 및 공통 컴포넌트 관리

## 1. 프로젝트 구조

```
mypets_voice/
├── backend/                    # Flask API 서버
│   ├── app.py                 # Flask 애플리케이션
│   ├── config.py              # 설정 파일
│   ├── requirements.txt       # Python 패키지
│   ├── models/                # 데이터베이스 모델
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── pet.py
│   │   ├── diary.py
│   │   └── community.py
│   ├── api/                   # API 라우트
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── chat.py
│   │   ├── diary.py
│   │   ├── community.py
│   │   ├── place.py
│   │   ├── tourspot.py
│   │   ├── dailycare.py
│   │   └── mypage.py
│   └── utils/                 # 유틸리티
│       ├── __init__.py
│       ├── helpers.py
│       └── decorators.py
├── frontend/                  # 프론트엔드 SPA
│   ├── index.html            # 메인 HTML (단일 페이지)
│   ├── css/
│   │   ├── base.css          # 기본 스타일
│   │   ├── components.css    # 공통 컴포넌트 스타일
│   │   ├── navbar.css        # 네비게이션
│   │   ├── footer.css        # 푸터
│   │   ├── chat.css          # 각 페이지별 스타일
│   │   ├── diary.css
│   │   ├── community.css
│   │   ├── place.css
│   │   ├── tourspot.css
│   │   ├── dailycare.css
│   │   └── mypage.css
│   ├── js/
│   │   ├── app.js           # 메인 애플리케이션
│   │   ├── router.js        # 클라이언트 라우터
│   │   ├── api.js           # API 통신 관리
│   │   ├── auth.js          # 인증 관리
│   │   ├── state.js         # 상태 관리
│   │   ├── components/      # 공통 컴포넌트들
│   │   │   ├── navbar.js
│   │   │   ├── footer.js
│   │   │   ├── modal.js
│   │   │   └── petCard.js
│   │   ├── pages/           # 각 페이지 모듈
│   │   │   ├── chat.js
│   │   │   ├── diary.js
│   │   │   ├── community.js
│   │   │   ├── place.js
│   │   │   ├── tourspot.js
│   │   │   ├── dailycare.js
│   │   │   └── mypage.js
│   │   └── utils/           # 유틸리티 함수
│   │       ├── helpers.js
│   │       ├── constants.js
│   │       └── validators.js
│   └── assets/              # 이미지, 폰트 등
│       └── images/
└── static/                  # Flask static 폴더 (개발 시만 사용)
    └── uploads/            # 업로드 파일들
```

## 2. 메인 HTML 파일 (frontend/index.html)

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MyPet's Voice</title>
    
    <!-- 외부 라이브러리 -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    
    <!-- CSS 파일들 -->
    <link rel="stylesheet" href="css/base.css">
    <link rel="stylesheet" href="css/components.css">
    <link rel="stylesheet" href="css/navbar.css">
    <link rel="stylesheet" href="css/footer.css">
    <link rel="stylesheet" href="css/chat.css">
    <link rel="stylesheet" href="css/diary.css">
    <link rel="stylesheet" href="css/community.css">
    <link rel="stylesheet" href="css/place.css">
    <link rel="stylesheet" href="css/tourspot.css">
    <link rel="stylesheet" href="css/dailycare.css">
    <link rel="stylesheet" href="css/mypage.css">
</head>
<body>
    <!-- 로딩 스피너 -->
    <div id="loading-spinner" class="loading-spinner hidden">
        <div class="spinner"></div>
    </div>
    
    <!-- 토스트 메시지 컨테이너 -->
    <div id="toast-container" class="toast-container"></div>
    
    <!-- 네비게이션 (동적으로 렌더링) -->
    <nav id="navbar-container"></nav>
    
    <!-- 메인 컨텐츠 영역 -->
    <main id="main-content" class="main-container">
        <!-- 페이지 컨텐츠가 동적으로 렌더링됩니다 -->
    </main>
    
    <!-- 푸터 (동적으로 렌더링) -->
    <footer id="footer-container"></footer>
    
    <!-- 모달 컨테이너 -->
    <div id="modal-container"></div>
    
    <!-- JavaScript 파일들 -->
    <!-- 유틸리티 및 공통 모듈 -->
    <script src="js/utils/constants.js"></script>
    <script src="js/utils/helpers.js"></script>
    <script src="js/utils/validators.js"></script>
    
    <!-- 핵심 시스템 모듈 -->
    <script src="js/api.js"></script>
    <script src="js/auth.js"></script>
    <script src="js/state.js"></script>
    <script src="js/router.js"></script>
    
    <!-- 공통 컴포넌트 -->
    <script src="js/components/navbar.js"></script>
    <script src="js/components/footer.js"></script>
    <script src="js/components/modal.js"></script>
    <script src="js/components/petCard.js"></script>
    
    <!-- 페이지 모듈 -->
    <script src="js/pages/chat.js"></script>
    <script src="js/pages/diary.js"></script>
    <script src="js/pages/community.js"></script>
    <script src="js/pages/place.js"></script>
    <script src="js/pages/tourspot.js"></script>
    <script src="js/pages/dailycare.js"></script>
    <script src="js/pages/mypage.js"></script>
    
    <!-- 메인 애플리케이션 -->
    <script src="js/app.js"></script>
</body>
</html>
```

## 3. 메인 애플리케이션 (js/app.js)

```javascript
class App {
    constructor() {
        this.router = null;
        this.authManager = null;
        this.stateManager = null;
        this.apiManager = null;
        
        this.init();
    }
    
    async init() {
        try {
            // 핵심 매니저들 초기화
            this.apiManager = new APIManager();
            this.authManager = new AuthManager();
            this.stateManager = new StateManager();
            this.router = new Router();
            
            // 공통 컴포넌트 렌더링
            await this.renderCommonComponents();
            
            // 라우터 초기화 및 시작
            this.initRouter();
            this.router.start();
            
            // 전역 이벤트 리스너 설정
            this.setupGlobalEvents();
            
            console.log('App initialized successfully');
        } catch (error) {
            console.error('App initialization failed:', error);
            this.showError('애플리케이션 초기화에 실패했습니다.');
        }
    }
    
    async renderCommonComponents() {
        // 네비게이션 렌더링
        const navbarComponent = new NavbarComponent();
        await navbarComponent.render();
        
        // 푸터 렌더링
        const footerComponent = new FooterComponent();
        await footerComponent.render();
    }
    
    initRouter() {
        // 라우트 등록
        this.router.addRoute('/', () => this.renderPage('home'));
        this.router.addRoute('/chat', () => this.renderPage('chat'));
        this.router.addRoute('/diary', () => this.renderPage('diary'));
        this.router.addRoute('/diary/create', () => this.renderPage('diary-create'));
        this.router.addRoute('/community', () => this.renderPage('community'));
        this.router.addRoute('/place', () => this.renderPage('place'));
        this.router.addRoute('/tourspot', () => this.renderPage('tourspot'));
        this.router.addRoute('/dailycare', () => this.renderPage('dailycare'));
        this.router.addRoute('/mypage', () => this.renderPage('mypage'));
        
        // 404 페이지
        this.router.setNotFoundHandler(() => this.renderPage('404'));
    }
    
    async renderPage(pageName) {
        const mainContent = document.getElementById('main-content');
        
        try {
            // 로딩 표시
            Utils.showLoading();
            
            // 페이지별 렌더링
            switch (pageName) {
                case 'home':
                    mainContent.innerHTML = this.getHomeTemplate();
                    break;
                case 'chat':
                    const chatPage = new ChatPage();
                    await chatPage.render();
                    break;
                case 'diary':
                    const diaryPage = new DiaryPage();
                    await diaryPage.render();
                    break;
                case 'community':
                    const communityPage = new CommunityPage();
                    await communityPage.render();
                    break;
                case 'place':
                    const placePage = new PlacePage();
                    await placePage.render();
                    break;
                case 'tourspot':
                    const tourspotPage = new TourspotPage();
                    await tourspotPage.render();
                    break;
                case 'dailycare':
                    const dailycarePage = new DailycarePage();
                    await dailycarePage.render();
                    break;
                case 'mypage':
                    const mypagePage = new MypagePage();
                    await mypagePage.render();
                    break;
                default:
                    mainContent.innerHTML = '<h1>페이지를 찾을 수 없습니다.</h1>';
            }
        } catch (error) {
            console.error('Page rendering failed:', error);
            mainContent.innerHTML = '<h1>페이지 로딩에 실패했습니다.</h1>';
        } finally {
            Utils.hideLoading();
        }
    }
    
    getHomeTemplate() {
        return `
            <div class="home-container">
                <div class="hero-section">
                    <h1>MyPet's Voice에 오신 것을 환영합니다!</h1>
                    <p>반려동물과의 특별한 대화를 경험해보세요.</p>
                    <div class="hero-buttons">
                        <button class="btn btn-primary" id="hero-login">로그인하기</button>
                        <button class="btn btn-outline" id="hero-signup">회원가입하기</button>
                    </div>
                </div>
            </div>
        `;
    }
    
    setupGlobalEvents() {
        // 전역 클릭 이벤트
        document.addEventListener('click', (e) => {
            this.handleGlobalClick(e);
        });
        
        // 브라우저 뒤로가기/앞으로가기
        window.addEventListener('popstate', (e) => {
            this.router.handlePopState(e);
        });
        
        // 네트워크 상태 변경
        window.addEventListener('online', () => {
            Utils.showToast('인터넷 연결이 복원되었습니다.', 'success');
        });
        
        window.addEventListener('offline', () => {
            Utils.showToast('인터넷 연결이 끊어졌습니다.', 'warning');
        });
    }
    
    handleGlobalClick(e) {
        // 내부 링크 처리
        if (e.target.matches('a[href^="/"]') || e.target.closest('a[href^="/"]')) {
            e.preventDefault();
            const link = e.target.matches('a') ? e.target : e.target.closest('a');
            this.router.navigate(link.getAttribute('href'));
            return;
        }
        
        // 버튼별 이벤트 처리
        const button = e.target.closest('button');
        if (!button) return;
        
        const action = button.dataset.action;
        if (action) {
            this.handleButtonAction(action, button);
        }
    }
    
    handleButtonAction(action, button) {
        switch (action) {
            case 'login':
                this.authManager.showLoginModal();
                break;
            case 'signup':
                this.authManager.showSignupModal();
                break;
            case 'logout':
                this.authManager.logout();
                break;
            // 추가 액션들...
        }
    }
    
    showError(message) {
        Utils.showToast(message, 'error');
    }
}

// DOM 로드 완료 시 앱 시작
document.addEventListener('DOMContentLoaded', () => {
    window.app = new App();
});
```

## 4. 클라이언트 라우터 (js/router.js)

```javascript
class Router {
    constructor() {
        this.routes = new Map();
        this.notFoundHandler = null;
        this.currentRoute = null;
    }
    
    addRoute(path, handler) {
        this.routes.set(path, handler);
    }
    
    setNotFoundHandler(handler) {
        this.notFoundHandler = handler;
    }
    
    start() {
        // 현재 URL에 맞는 페이지 로드
        this.handleRoute(window.location.pathname);
    }
    
    navigate(path) {
        // 히스토리 추가
        window.history.pushState(null, '', path);
        this.handleRoute(path);
    }
    
    handleRoute(path) {
        this.currentRoute = path;
        
        const handler = this.routes.get(path);
        if (handler) {
            handler();
        } else {
            // 동적 라우트 확인 (예: /diary/:id)
            const matchedRoute = this.findDynamicRoute(path);
            if (matchedRoute) {
                matchedRoute.handler(matchedRoute.params);
            } else if (this.notFoundHandler) {
                this.notFoundHandler();
            }
        }
    }
    
    findDynamicRoute(path) {
        // 동적 라우트 매칭 로직
        // 예: /diary/:id -> /diary/123
        for (const [route, handler] of this.routes) {
            const routeRegex = this.createRouteRegex(route);
            const match = path.match(routeRegex);
            if (match) {
                const params = this.extractParams(route, match);
                return { handler, params };
            }
        }
        return null;
    }
    
    createRouteRegex(route) {
        // :param을 정규식으로 변환
        const regexString = route
            .replace(/:[^/]+/g, '([^/]+)')
            .replace(/\//g, '\\/');
        return new RegExp(`^${regexString}$`);
    }
    
    extractParams(route, match) {
        const paramNames = route.match(/:[^/]+/g) || [];
        const params = {};
        
        paramNames.forEach((param, index) => {
            const paramName = param.substring(1); // ':' 제거
            params[paramName] = match[index + 1];
        });
        
        return params;
    }
    
    handlePopState(e) {
        this.handleRoute(window.location.pathname);
    }
}
```

## 5. API 매니저 (js/api.js)

```javascript
class APIManager {
    constructor() {
        this.baseURL = 'http://localhost:5000/api'; // Flask API 서버 주소
        this.token = localStorage.getItem('auth_token');
    }
    
    async request(endpoint, options = {}) {
        const url = `${this.baseURL}${endpoint}`;
        
        const config = {
            headers: {
                'Content-Type': 'application/json',
                ...options.headers
            },
            ...options
        };
        
        // 인증 토큰 추가
        if (this.token) {
            config.headers['Authorization'] = `Bearer ${this.token}`;
        }
        
        try {
            const response = await fetch(url, config);
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            return await response.json();
        } catch (error) {
            console.error('API request failed:', error);
            throw error;
        }
    }
    
    // 인증 관련 API
    async login(credentials) {
        return this.request('/auth/login', {
            method: 'POST',
            body: JSON.stringify(credentials)
        });
    }
    
    async signup(userData) {
        return this.request('/auth/signup', {
            method: 'POST',
            body: JSON.stringify(userData)
        });
    }
    
    // 반려동물 관련 API
    async getPets() {
        return this.request('/pets');
    }
    
    async createPet(petData) {
        return this.request('/pets', {
            method: 'POST',
            body: JSON.stringify(petData)
        });
    }
    
    // 일기 관련 API
    async getDiaries(params = {}) {
        const queryString = new URLSearchParams(params).toString();
        return this.request(`/diaries?${queryString}`);
    }
    
    async createDiary(diaryData) {
        return this.request('/diaries', {
            method: 'POST',
            body: JSON.stringify(diaryData)
        });
    }
    
    // 커뮤니티 관련 API
    async getCommunityPosts(params = {}) {
        const queryString = new URLSearchParams(params).toString();
        return this.request(`/community?${queryString}`);
    }
    
    // 채팅 관련 API
    async sendChatMessage(message, petId) {
        return this.request('/chat/message', {
            method: 'POST',
            body: JSON.stringify({ message, pet_id: petId })
        });
    }
    
    setAuthToken(token) {
        this.token = token;
        localStorage.setItem('auth_token', token);
    }
    
    removeAuthToken() {
        this.token = null;
        localStorage.removeItem('auth_token');
    }
}
```

## 6. 네비게이션 컴포넌트 (js/components/navbar.js)

```javascript
class NavbarComponent {
    constructor() {
        this.container = document.getElementById('navbar-container');
    }
    
    async render() {
        const isLoggedIn = window.app.authManager.isLoggedIn();
        const user = window.app.authManager.getCurrentUser();
        
        this.container.innerHTML = this.getTemplate(isLoggedIn, user);
        this.attachEvents();
    }
    
    getTemplate(isLoggedIn, user) {
        return `
            <div class="nav-container">
                <a href="/" class="nav-link nav-logo">
                    <i class="fas fa-paw"></i>
                    <span>MyPet's Voice</span>
                </a>
                
                <button class="mobile-menu-toggle" id="mobile-menu-toggle">
                    <i class="fas fa-bars"></i>
                </button>
                
                <div class="nav-menu" id="nav-menu">
                    <a href="/diary" class="nav-link">너의 일기장</a>
                    <a href="/community" class="nav-link">커뮤니티</a>
                    <a href="/place" class="nav-link">플레이스</a>
                    <a href="/tourspot" class="nav-link">투어스팟</a>
                    <a href="/dailycare" class="nav-link">데일리케어</a>
                    <a href="/mypage" class="nav-link">마이페이지</a>
                </div>

                <div class="nav-user">
                    ${isLoggedIn ? this.getLoggedInTemplate(user) : this.getLoggedOutTemplate()}
                </div>
            </div>
        `;
    }
    
    getLoggedInTemplate(user) {
        return `
            <div class="user-menu">
                <button class="user-avatar" id="user-menu-btn">
                    <img src="${user.avatar || 'assets/images/default-avatar.png'}" alt="프로필">
                </button>
                <div class="user-dropdown" id="user-dropdown">
                    <a href="/mypage">마이페이지</a>
                    <button data-action="logout">로그아웃</button>
                </div>
            </div>
        `;
    }
    
    getLoggedOutTemplate() {
        return `
            <button class="btn btn-primary" data-action="login">
                <i class="fas fa-sign-in-alt"></i> 로그인
            </button>
            <button class="btn btn-outline" data-action="signup">
                회원가입
            </button>
        `;
    }
    
    attachEvents() {
        // 모바일 메뉴 토글
        const mobileToggle = document.getElementById('mobile-menu-toggle');
        const navMenu = document.getElementById('nav-menu');
        
        if (mobileToggle) {
            mobileToggle.addEventListener('click', () => {
                navMenu.classList.toggle('active');
            });
        }
        
        // 사용자 메뉴 토글
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
        
        // 현재 페이지 활성화 표시
        this.setActiveNavItem();
    }
    
    setActiveNavItem() {
        const currentPath = window.location.pathname;
        const navLinks = this.container.querySelectorAll('.nav-link');
        
        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === currentPath) {
                link.classList.add('active');
            }
        });
    }
    
    // 로그인 상태 변경 시 네비게이션 업데이트
    updateAuthState() {
        this.render();
    }
}
```

## 7. 페이지 예시 - 일기 페이지 (js/pages/diary.js)

```javascript
class DiaryPage {
    constructor() {
        this.container = document.getElementById('main-content');
        this.diaries = [];
        this.currentFilter = 'my';
        this.selectedPet = null;
    }
    
    async render() {
        this.container.innerHTML = this.getTemplate();
        await this.loadData();
        this.attachEvents();
    }
    
    getTemplate() {
        return `
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
                    </select>
                    <div class="view-toggle">
                        <button class="view-btn active" data-view="my">내 일기</button>
                        <button class="view-btn" data-view="public">공개 일기</button>
                    </div>
                </div>

                <div class="diary-grid" id="diary-grid">
                    <!-- 일기 카드들이 동적으로 렌더링됩니다 -->
                </div>
            </div>
        `;
    }
    
    async loadData() {
        try {
            // 반려동물 목록 로드
            const pets = await window.app.apiManager.getPets();
            this.renderPetFilter(pets);
            
            // 일기 목록 로드
            await this.loadDiaries();
        } catch (error) {
            console.error('Failed to load diary data:', error);
            Utils.showToast('데이터 로딩에 실패했습니다.', 'error');
        }
    }
    
    renderPetFilter(pets) {
        const petFilter = document.getElementById('diary-pet-filter');
        pets.forEach(pet => {
            const option = document.createElement('option');
            option.value = pet.id;
            option.textContent = pet.name;
            petFilter.appendChild(option);
        });
    }
    
    async loadDiaries() {
        try {
            const params = {
                filter: this.currentFilter,
                pet_id: this.selectedPet
            };
            
            this.diaries = await window.app.apiManager.getDiaries(params);
            this.renderDiaries();
        } catch (error) {
            console.error('Failed to load diaries:', error);
        }
    }
    
    renderDiaries() {
        const grid = document.getElementById('diary-grid');
        
        if (this.diaries.length === 0) {
            grid.innerHTML = '<div class="no-data">작성된 일기가 없습니다.</div>';
            return;
        }
        
        grid.innerHTML = this.diaries.map(diary => this.getDiaryCardTemplate(diary)).join('');
    }
    
    getDiaryCardTemplate(diary) {
        return `
            <div class="diary-card" data-diary-id="${diary.id}">
                <div class="diary-image">
                    ${diary.images ? `<img src="${diary.images[0]}" alt="일기 이미지">` : diary.pet_emoji}
                </div>
                <div class="diary-content">
                    <div class="diary-meta">
                        <span>${Utils.formatDate(diary.created_at)}</span>
                        <span>${diary.weather} ${diary.temperature}°C</span>
                    </div>
                    <div class="diary-title">${diary.title}</div>
                    <div class="diary-preview">${diary.content.substring(0, 100)}...</div>
                    <div class="diary-footer">
                        <div class="diary-pet">
                            <div class="diary-pet-avatar">${diary.pet_emoji}</div>
                            <span>${diary.pet_name}</span>
                        </div>
                        <div class="diary-stats">
                            <span>❤️ ${diary.likes_count}</span>
                            <span>👀 ${diary.views_count}</span>
                        </div>
                    </div>
                </div>
            </div>
        `;
    }
    
    attachEvents() {
        // 일기 작성 버튼
        document.getElementById('create-diary-btn').addEventListener('click', () => {
            window.app.router.navigate('/diary/create');
        });
        
        // 필터 변경
        document.getElementById('diary-pet-filter').addEventListener('change', (e) => {
            this.selectedPet = e.target.value || null;
            this.loadDiaries();
        });
        
        // 뷰 토글
        document.querySelectorAll('.view-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                document.querySelectorAll('.view-btn').forEach(b => b.classList.remove('active'));
                e.target.classList.add('active');
                this.currentFilter = e.target.dataset.view;
                this.loadDiaries();
            });
        });
        
        // 일기 카드 클릭
        document.getElementById('diary-grid').addEventListener('click', (e) => {
            const diaryCard = e.target.closest('.diary-card');
            if (diaryCard) {
                const diaryId = diaryCard.dataset.diaryId;
                window.app.router.navigate(`/diary/${diaryId}`);
            }
        });
    }
}

## 8. 상태 관리 (js/state.js)

```javascript
class StateManager {
    constructor() {
        this.state = {
            user: null,
            pets: [],
            currentPet: null,
            isLoggedIn: false,
            theme: 'light'
        };
        
        this.listeners = new Map();
        this.loadFromStorage();
    }
    
    // 상태 변경
    setState(newState) {
        const prevState = { ...this.state };
        this.state = { ...this.state, ...newState };
        
        // 변경된 키들에 대해 리스너 호출
        Object.keys(newState).forEach(key => {
            if (prevState[key] !== this.state[key]) {
                this.notifyListeners(key, this.state[key], prevState[key]);
            }
        });
        
        this.saveToStorage();
    }
    
    // 상태 조회
    getState(key) {
        return key ? this.state[key] : this.state;
    }
    
    // 상태 변경 리스너 등록
    subscribe(key, callback) {
        if (!this.listeners.has(key)) {
            this.listeners.set(key, []);
        }
        this.listeners.get(key).push(callback);
        
        // 구독 해제 함수 반환
        return () => {
            const callbacks = this.listeners.get(key);
            const index = callbacks.indexOf(callback);
            if (index > -1) {
                callbacks.splice(index, 1);
            }
        };
    }
    
    // 리스너들에게 알림
    notifyListeners(key, newValue, oldValue) {
        const callbacks = this.listeners.get(key);
        if (callbacks) {
            callbacks.forEach(callback => {
                try {
                    callback(newValue, oldValue);
                } catch (error) {
                    console.error('State listener error:', error);
                }
            });
        }
    }
    
    // 로컬 스토리지에서 로드
    loadFromStorage() {
        try {
            const saved = localStorage.getItem('app_state');
            if (saved) {
                const parsedState = JSON.parse(saved);
                this.state = { ...this.state, ...parsedState };
            }
        } catch (error) {
            console.error('Failed to load state from storage:', error);
        }
    }
    
    // 로컬 스토리지에 저장
    saveToStorage() {
        try {
            const stateToSave = {
                user: this.state.user,
                theme: this.state.theme,
                isLoggedIn: this.state.isLoggedIn
            };
            localStorage.setItem('app_state', JSON.stringify(stateToSave));
        } catch (error) {
            console.error('Failed to save state to storage:', error);
        }
    }
    
    // 상태 초기화
    reset() {
        this.state = {
            user: null,
            pets: [],
            currentPet: null,
            isLoggedIn: false,
            theme: 'light'
        };
        localStorage.removeItem('app_state');
    }
}

## 9. 인증 매니저 (js/auth.js)

```javascript
class AuthManager {
    constructor() {
        this.apiManager = null;
        this.stateManager = null;
        this.init();
    }
    
    init() {
        // 다른 매니저들이 초기화된 후 설정
        setTimeout(() => {
            this.apiManager = window.app.apiManager;
            this.stateManager = window.app.stateManager;
            this.checkAuthStatus();
        }, 0);
    }
    
    async checkAuthStatus() {
        const token = localStorage.getItem('auth_token');
        if (token) {
            try {
                // 토큰 유효성 검증
                const user = await this.apiManager.request('/auth/me');
                this.setUser(user);
            } catch (error) {
                console.log('Token invalid, logging out');
                this.logout();
            }
        }
    }
    
    async login(credentials) {
        try {
            const response = await this.apiManager.login(credentials);
            
            if (response.success) {
                this.apiManager.setAuthToken(response.token);
                this.setUser(response.user);
                Utils.showToast('로그인에 성공했습니다.', 'success');
                return true;
            } else {
                Utils.showToast(response.message || '로그인에 실패했습니다.', 'error');
                return false;
            }
        } catch (error) {
            console.error('Login error:', error);
            Utils.showToast('로그인 중 오류가 발생했습니다.', 'error');
            return false;
        }
    }
    
    async signup(userData) {
        try {
            const response = await this.apiManager.signup(userData);
            
            if (response.success) {
                Utils.showToast('회원가입이 완료되었습니다. 로그인해주세요.', 'success');
                return true;
            } else {
                Utils.showToast(response.message || '회원가입에 실패했습니다.', 'error');
                return false;
            }
        } catch (error) {
            console.error('Signup error:', error);
            Utils.showToast('회원가입 중 오류가 발생했습니다.', 'error');
            return false;
        }
    }
    
    logout() {
        this.apiManager.removeAuthToken();
        this.stateManager.reset();
        
        // 네비게이션 업데이트
        const navbar = document.querySelector('navbar-component');
        if (navbar) {
            navbar.updateAuthState();
        }
        
        // 홈페이지로 리다이렉트
        window.app.router.navigate('/');
        
        Utils.showToast('로그아웃되었습니다.', 'info');
    }
    
    setUser(user) {
        this.stateManager.setState({
            user: user,
            isLoggedIn: true
        });
        
        // 네비게이션 업데이트
        this.updateNavbar();
    }
    
    isLoggedIn() {
        return this.stateManager.getState('isLoggedIn');
    }
    
    getCurrentUser() {
        return this.stateManager.getState('user');
    }
    
    updateNavbar() {
        const navbarComponent = new NavbarComponent();
        navbarComponent.render();
    }
    
    showLoginModal() {
        const modal = new Modal();
        modal.show({
            title: '로그인',
            content: this.getLoginModalContent(),
            onShow: () => this.attachLoginEvents(modal)
        });
    }
    
    getLoginModalContent() {
        return `
            <form id="login-form" class="auth-form">
                <div class="form-group">
                    <label for="login-email">이메일</label>
                    <input type="email" id="login-email" required>
                </div>
                <div class="form-group">
                    <label for="login-password">비밀번호</label>
                    <input type="password" id="login-password" required>
                </div>
                <div class="form-actions">
                    <button type="submit" class="btn btn-primary">로그인</button>
                    <button type="button" class="btn btn-outline" id="show-signup">회원가입</button>
                </div>
                <div class="social-login">
                    <button type="button" class="btn btn-kakao" id="kakao-login">
                        카카오 로그인
                    </button>
                    <button type="button" class="btn btn-naver" id="naver-login">
                        네이버 로그인
                    </button>
                    <button type="button" class="btn btn-google" id="google-login">
                        구글 로그인
                    </button>
                </div>
            </form>
        `;
    }
    
    attachLoginEvents(modal) {
        const form = document.getElementById('login-form');
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const email = document.getElementById('login-email').value;
            const password = document.getElementById('login-password').value;
            
            const success = await this.login({ email, password });
            if (success) {
                modal.hide();
            }
        });
        
        document.getElementById('show-signup').addEventListener('click', () => {
            modal.hide();
            this.showSignupModal();
        });
        
        // 소셜 로그인 버튼들
        document.getElementById('kakao-login').addEventListener('click', () => {
            this.handleSocialLogin('kakao');
        });
        
        document.getElementById('naver-login').addEventListener('click', () => {
            this.handleSocialLogin('naver');
        });
        
        document.getElementById('google-login').addEventListener('click', () => {
            this.handleSocialLogin('google');
        });
    }
    
    showSignupModal() {
        const modal = new Modal();
        modal.show({
            title: '회원가입',
            content: this.getSignupModalContent(),
            onShow: () => this.attachSignupEvents(modal)
        });
    }
    
    getSignupModalContent() {
        return `
            <form id="signup-form" class="auth-form">
                <div class="form-group">
                    <label for="signup-name">이름</label>
                    <input type="text" id="signup-name" required>
                </div>
                <div class="form-group">
                    <label for="signup-email">이메일</label>
                    <input type="email" id="signup-email" required>
                    <button type="button" class="btn btn-sm" id="verify-email">인증</button>
                </div>
                <div class="form-group">
                    <label for="signup-nickname">닉네임</label>
                    <input type="text" id="signup-nickname" required>
                </div>
                <div class="form-group">
                    <label for="signup-password">비밀번호</label>
                    <input type="password" id="signup-password" required>
                </div>
                <div class="form-group">
                    <label for="signup-password-confirm">비밀번호 확인</label>
                    <input type="password" id="signup-password-confirm" required>
                </div>
                <div class="form-actions">
                    <button type="submit" class="btn btn-primary">회원가입</button>
                    <button type="button" class="btn btn-outline" id="show-login">로그인</button>
                </div>
            </form>
        `;
    }
    
    attachSignupEvents(modal) {
        const form = document.getElementById('signup-form');
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const formData = new FormData(form);
            const userData = Object.fromEntries(formData);
            
            // 비밀번호 확인
            if (userData.password !== userData.passwordConfirm) {
                Utils.showToast('비밀번호가 일치하지 않습니다.', 'error');
                return;
            }
            
            const success = await this.signup(userData);
            if (success) {
                modal.hide();
                this.showLoginModal();
            }
        });
        
        document.getElementById('show-login').addEventListener('click', () => {
            modal.hide();
            this.showLoginModal();
        });
    }
    
    async handleSocialLogin(provider) {
        // 소셜 로그인 처리
        try {
            const popup = window.open(
                `${this.apiManager.baseURL}/auth/${provider}`,
                'social-login',
                'width=500,height=600'
            );
            
            // 팝업에서 완료 메시지 대기
            const handleMessage = (event) => {
                if (event.data.type === 'social-login-success') {
                    this.apiManager.setAuthToken(event.data.token);
                    this.setUser(event.data.user);
                    popup.close();
                    window.removeEventListener('message', handleMessage);
                }
            };
            
            window.addEventListener('message', handleMessage);
        } catch (error) {
            console.error('Social login error:', error);
            Utils.showToast('소셜 로그인 중 오류가 발생했습니다.', 'error');
        }
    }
}

## 10. 유틸리티 함수 (js/utils/helpers.js)

```javascript
class Utils {
    static showLoading() {
        const spinner = document.getElementById('loading-spinner');
        if (spinner) {
            spinner.classList.remove('hidden');
        }
    }
    
    static hideLoading() {
        const spinner = document.getElementById('loading-spinner');
        if (spinner) {
            spinner.classList.add('hidden');
        }
    }
    
    static showToast(message, type = 'info', duration = 3000) {
        const container = document.getElementById('toast-container');
        if (!container) return;
        
        const toast = document.createElement('div');
        toast.className = `toast toast-${type}`;
        toast.innerHTML = `
            <div class="toast-content">
                <i class="fas ${this.getToastIcon(type)}"></i>
                <span>${message}</span>
            </div>
            <button class="toast-close" onclick="this.parentElement.remove()">
                <i class="fas fa-times"></i>
            </button>
        `;
        
        container.appendChild(toast);
        
        // 애니메이션
        setTimeout(() => toast.classList.add('show'), 10);
        
        // 자동 제거
        setTimeout(() => {
            toast.classList.remove('show');
            setTimeout(() => toast.remove(), 300);
        }, duration);
    }
    
    static getToastIcon(type) {
        const icons = {
            success: 'fa-check-circle',
            error: 'fa-exclamation-circle',
            warning: 'fa-exclamation-triangle',
            info: 'fa-info-circle'
        };
        return icons[type] || icons.info;
    }
    
    static formatDate(dateString) {
        const date = new Date(dateString);
        const now = new Date();
        const diff = now - date;
        
        // 1일 이내
        if (diff < 24 * 60 * 60 * 1000) {
            const hours = Math.floor(diff / (60 * 60 * 1000));
            if (hours === 0) {
                const minutes = Math.floor(diff / (60 * 1000));
                return `${minutes}분 전`;
            }
            return `${hours}시간 전`;
        }
        
        // 1주일 이내
        if (diff < 7 * 24 * 60 * 60 * 1000) {
            const days = Math.floor(diff / (24 * 60 * 60 * 1000));
            return `${days}일 전`;
        }
        
        // 그 외
        return date.toLocaleDateString('ko-KR');
    }
    
    static debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }
    
    static throttle(func, limit) {
        let inThrottle;
        return function() {
            const args = arguments;
            const context = this;
            if (!inThrottle) {
                func.apply(context, args);
                inThrottle = true;
                setTimeout(() => inThrottle = false, limit);
            }
        };
    }
    
    static async uploadFile(file, endpoint) {
        const formData = new FormData();
        formData.append('file', file);
        
        try {
            const response = await fetch(endpoint, {
                method: 'POST',
                body: formData,
                headers: {
                    'Authorization': `Bearer ${localStorage.getItem('auth_token')}`
                }
            });
            
            if (!response.ok) {
                throw new Error('Upload failed');
            }
            
            return await response.json();
        } catch (error) {
            console.error('File upload error:', error);
            throw error;
        }
    }
    
    static validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }
    
    static validatePassword(password) {
        // 최소 8자, 영문, 숫자, 특수문자 포함
        const re = /^(?=.*[a-zA-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
        return re.test(password);
    }
    
    static getFileExtension(filename) {
        return filename.split('.').pop().toLowerCase();
    }
    
    static formatFileSize(bytes) {
        if (bytes === 0) return '0 Bytes';
        
        const k = 1024;
        const sizes = ['Bytes', 'KB', 'MB', 'GB'];
        const i = Math.floor(Math.log(bytes) / Math.log(k));
        
        return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
    }
}

// 전역으로 사용할 수 있도록 설정
window.Utils = Utils;

## 11. Flask API 서버 예시 (backend/app.py)

```python
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
import sqlite3
import os
from datetime import timedelta

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your-secret-key'  # 실제로는 환경변수로 관리
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=24)

# CORS 설정 (개발 시에만)
CORS(app, origins=['http://localhost:3000', 'http://127.0.0.1:3000'])

jwt = JWTManager(app)

# 데이터베이스 초기화
def init_db():
    conn = sqlite3.connect('mypets.db')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            nickname TEXT NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS pets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            species TEXT NOT NULL,
            breed TEXT,
            age INTEGER,
            personality TEXT,
            speaking_style TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    conn.commit()
    conn.close()

# API 라우트
@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    # 실제로는 비밀번호 해싱 확인 필요
    conn = sqlite3.connect('mypets.db')
    user = conn.execute(
        'SELECT * FROM users WHERE email = ?', (email,)
    ).fetchone()
    conn.close()
    
    if user:  # 실제로는 비밀번호 검증 필요
        access_token = create_access_token(identity=user[0])
        return jsonify({
            'success': True,
            'token': access_token,
            'user': {
                'id': user[0],
                'email': user[1],
                'name': user[2],
                'nickname': user[3]
            }
        })
    
    return jsonify({'success': False, 'message': '로그인 정보가 올바르지 않습니다.'}), 401

@app.route('/api/auth/me', methods=['GET'])
@jwt_required()
def get_current_user():
    user_id = get_jwt_identity()
    
    conn = sqlite3.connect('mypets.db')
    user = conn.execute(
        'SELECT * FROM users WHERE id = ?', (user_id,)
    ).fetchone()
    conn.close()
    
    if user:
        return jsonify({
            'id': user[0],
            'email': user[1],
            'name': user[2],
            'nickname': user[3]
        })
    
    return jsonify({'error': 'User not found'}), 404

@app.route('/api/pets', methods=['GET'])
@jwt_required()
def get_pets():
    user_id = get_jwt_identity()
    
    conn = sqlite3.connect('mypets.db')
    pets = conn.execute(
        'SELECT * FROM pets WHERE user_id = ?', (user_id,)
    ).fetchall()
    conn.close()
    
    pets_list = []
    for pet in pets:
        pets_list.append({
            'id': pet[0],
            'name': pet[2],
            'species': pet[3],
            'breed': pet[4],
            'age': pet[5],
            'personality': pet[6],
            'speaking_style': pet[7]
        })
    
    return jsonify(pets_list)

@app.route('/api/diaries', methods=['GET'])
@jwt_required()
def get_diaries():
    user_id = get_jwt_identity()
    filter_type = request.args.get('filter', 'my')
    pet_id = request.args.get('pet_id')
    
    # 실제 구현에서는 더 복잡한 쿼리와 조건 처리 필요
    # 임시 데이터 반환
    sample_diaries = [
        {
            'id': 1,
            'title': '오늘 산책이 너무 즐거웠어!',
            'content': '주인님과 함께한 한강공원 산책이 정말 행복했어...',
            'pet_name': '멍멍이',
            'pet_emoji': '🐕',
            'created_at': '2025-01-10T10:00:00Z',
            'weather': '☀️ 맑음',
            'temperature': 15,
            'likes_count': 15,
            'views_count': 32,
            'images': []
        }
    ]
    
    return jsonify(sample_diaries)

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)
```

## 12. 개발자별 작업 가이드

### 각 개발자가 담당할 파일들:

**채팅 담당자:**
- `frontend/js/pages/chat.js`
- `frontend/css/chat.css`
- `backend/api/chat.py`

**일기 담당자:**
- `frontend/js/pages/diary.js`
- `frontend/css/diary.css`
- `backend/api/diary.py`

**커뮤니티 담당자:**
- `frontend/js/pages/community.js`
- `frontend/css/community.css`
- `backend/api/community.py`

**나머지 기능들도 동일한 패턴**

### 협업 규칙:
1. **공통 파일 수정 금지**: `app.js`, `router.js`, `api.js`, `navbar.js`, `footer.js` 등
2. **API 엔드포인트 규칙**: `/api/모듈명/기능` 형태로 통일
3. **CSS 클래스 네이밍**: `모듈명-요소명` 형태로 충돌 방지
4. **상태 관리**: StateManager를 통해서만 전역 상태 변경

## SPA 방식의 장점:
1. **빠른 페이지 전환**: 새로고침 없이 부드러운 전환
2. **개발 분리**: 프론트엔드와 백엔드 완전 분리
3. **API 재사용**: 모바일 앱 등에서 동일한 API 사용 가능
4. **현대적인 UX**: SPA 특유의 빠른 반응성
5. **배포 유연성**: 프론트엔드와 백엔드 별도 배포 가능

이 구조로 진행하시면 각 개발자가 독립적으로 작업하면서도 통합된 애플리케이션을 만들 수 있습니다!