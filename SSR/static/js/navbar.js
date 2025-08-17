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

document.addEventListener('DOMContentLoaded', () => {
    new NavbarManager();
});