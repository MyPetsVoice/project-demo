class AuthManager {
    constructor() {
        this.init();
    }
    
    init() {
        this.checkLoginStatus();
    }
    
    checkLoginStatus() {
        // TODO: 로그인 상태 확인 로직
    }
    
    async login(username, password) {
        try {
            const response = await fetch('/auth/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ username, password })
            });
            
            if (response.ok) {
                window.location.reload();
            } else {
                throw new Error('로그인 실패');
            }
        } catch (error) {
            CommonUtils.showToast('로그인에 실패했습니다.', 'error');
        }
    }
    
    async logout() {
        try {
            const response = await fetch('/auth/logout', {
                method: 'POST'
            });
            
            if (response.ok) {
                window.location.href = '/';
            }
        } catch (error) {
            CommonUtils.showToast('로그아웃에 실패했습니다.', 'error');
        }
    }
}

document.addEventListener('DOMContentLoaded', () => {
    new AuthManager();
});