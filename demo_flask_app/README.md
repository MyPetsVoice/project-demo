# PetCare - 반려동물 종합 케어 서비스

생성형 AI를 이용한 반려동물 종합 관리 서비스입니다.

## 주요 기능

### 🤖 AI 기반 서비스
- **AI 반려동물 채팅**: 반려동물의 개성을 반영한 맞춤형 AI 채팅
- **AI 일기 작성**: 반려동물 관점에서 작성되는 감동적인 일기

### 🐕 반려동물 관리
- **프로필 관리**: 반려동물 정보 등록 및 관리
- **건강 관리**: 건강 기록, 병력 관리
- **케어 루틴**: 일상 케어 루틴 관리 및 알림

### 👥 커뮤니티
- **게시판**: 반려동물 관련 정보 공유
- **일기 공유**: 반려동물 일기 공개 및 좋아요

### 📍 위치 기반 서비스
- **장소 찾기**: 반려동물 관련 장소 검색 (카카오맵 API)
- **여행지 정보**: 반려동물 동반 가능 여행지 정보

## 기술 스택

### Backend
- **Framework**: Flask 2.3.3
- **Database**: SQLite (개발용), PostgreSQL (운영용)
- **ORM**: SQLAlchemy
- **Authentication**: Flask-Login

### Frontend
- **Template Engine**: Jinja2
- **CSS Framework**: Bootstrap 5
- **JavaScript**: Vanilla JS + Custom Utils

### AI/ML
- **LLM**: OpenAI GPT-3.5-turbo
- **TTS**: 추후 구현 예정

### External APIs
- **카카오맵 API**: 지도 및 장소 검색
- **날씨 API**: 일기 작성용
- **소셜 로그인**: 카카오, 네이버, 구글 OAuth

## 설치 및 실행

### 1. 의존성 설치
```bash
pip install -r requirements.txt
```

### 2. 환경변수 설정
`.env.example` 파일을 참고하여 `.env` 파일을 생성하고 API 키들을 설정하세요.

**중요**: OpenAI API 키가 있어야 AI 채팅 기능이 정상 작동합니다.

### 3. 데이터베이스 초기화
```bash
python app.py
```
첫 실행 시 자동으로 데이터베이스가 생성됩니다.

### 4. 서버 실행
```bash
python app.py
```

서버가 `http://localhost:5000`에서 실행됩니다.

## 데모 계정

### 테스트 사용자 생성
1. 회원가입 페이지에서 계정 생성
2. 반려동물 등록
3. 모든 기능 체험 가능

### 샘플 데이터
- 일기 샘플
- 커뮤니티 게시글 샘플
- 장소 정보 샘플
- 여행지 정보 샘플

## 프로젝트 구조

```
Team3_Project/
├── app.py                 # 메인 애플리케이션
├── models.py              # 데이터베이스 모델
├── requirements.txt       # 의존성 패키지
├── .env                   # 환경변수 (실제 키 포함)
├── .env.example          # 환경변수 템플릿
├── templates/            # HTML 템플릿
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── pets.html
│   ├── add_pet.html
│   ├── chat.html
│   ├── diary_list.html
│   ├── write_diary.html
│   ├── pet_diary.html
│   ├── community.html
│   ├── write_post.html
│   ├── care.html
│   ├── pet_care.html
│   ├── places.html
│   └── travel.html
├── static/
│   ├── css/
│   │   └── style.css      # 커스텀 스타일
│   ├── js/
│   │   └── main.js        # 커스텀 JavaScript
│   └── uploads/           # 업로드 파일 저장소
└── srs.txt               # 서비스 요구사항 정의서
```

## 주요 페이지

### 🏠 메인 페이지 (`/`)
- 서비스 소개
- 인기 일기 및 게시글
- 주요 기능 안내

### 👤 사용자 관리
- **회원가입** (`/register`): 이메일 인증, 유효성 검사
- **로그인** (`/login`): 자체 로그인 + 소셜 로그인
- **대시보드** (`/dashboard`): 개인 현황 및 빠른 액션

### 🐾 반려동물 관리
- **반려동물 목록** (`/pets`): 등록된 반려동물 관리
- **반려동물 등록** (`/pets/add`): 새 반려동물 등록
- **AI 채팅** (`/chat/<pet_id>`): 반려동물별 AI 채팅

### 📖 일기 서비스
- **일기 목록** (`/diary`): 반려동물별 일기 선택
- **일기 작성** (`/diary/write/<pet_id>`): AI 기반 일기 생성
- **일기 보기** (`/diary/<pet_id>`): 작성된 일기 관리

### 💬 커뮤니티
- **게시판** (`/community`): 커뮤니티 게시글 목록
- **글 작성** (`/community/write`): 새 게시글 작성

### 🏥 케어 관리
- **케어 목록** (`/care`): 반려동물별 케어 선택
- **케어 관리** (`/care/<pet_id>`): 건강 기록 및 루틴 관리

### 📍 위치 서비스
- **장소 찾기** (`/places`): 반려동물 관련 장소 검색
- **여행지** (`/travel`): 반려동물 동반 여행지 정보

## API 엔드포인트

### 인증 API
- `POST /register` - 회원가입
- `POST /login` - 로그인
- `GET /logout` - 로그아웃

### 반려동물 API
- `GET /pets` - 반려동물 목록
- `POST /pets/add` - 반려동물 등록

### AI 채팅 API
- `POST /api/chat` - AI 채팅 메시지 전송

### 일기 API
- `POST /diary/write/<pet_id>` - AI 일기 생성

### 커뮤니티 API
- `POST /community/write` - 게시글 작성

## 개발 상태

### ✅ 완료된 기능
- 회원가입/로그인 시스템
- 반려동물 프로필 관리
- AI 채팅 기능 (OpenAI GPT-3.5)
- AI 일기 작성
- 커뮤니티 기본 기능
- 반려동물 케어 관리 기본 틀
- 지도/여행지 정보 UI

### 🚧 구현 예정
- 소셜 로그인 연동
- 파일 업로드 기능
- 실시간 알림
- TTS 음성 기능
- 카카오맵 API 연동
- 날씨 API 연동
- 이메일 인증
- 좋아요/북마크 기능
- 댓글/대댓글 시스템
- 무한 스크롤
- 관리자 기능

## 주의사항

### API 키 설정
1. **OpenAI API 키**: AI 채팅 및 일기 기능 필수
2. **카카오맵 API 키**: 지도 서비스용
3. **소셜 로그인 키**: OAuth 연동용

### 보안
- 실제 배포 시 SECRET_KEY 변경 필요
- API 키들은 환경변수로 관리
- 파일 업로드 시 보안 검증 필요

### 성능
- 대용량 트래픽 시 데이터베이스 최적화 필요
- AI API 호출 비용 고려
- CDN 및 캐싱 적용 권장

## 라이선스

이 프로젝트는 교육용 데모 프로젝트입니다.

## 개발팀

- SESAC Python Team 3
- 생성형 AI 활용 서비스 개발 프로젝트

---

**📧 문의사항**: 프로젝트 관련 문의는 이슈를 생성해주세요.

**🔗 참고자료**:
- [Flask 공식 문서](https://flask.palletsprojects.com/)
- [OpenAI API 문서](https://platform.openai.com/docs)
- [카카오맵 API 문서](https://apis.map.kakao.com/)