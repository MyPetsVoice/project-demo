// PetCare 메인 JavaScript 파일

// 전역 유틸리티 함수들
const Utils = {
    // API 호출 헬퍼
    async apiCall(url, method = 'GET', data = null) {
        const options = {
            method: method,
            headers: {
                'Content-Type': 'application/json',
            }
        };
        
        if (data) {
            options.body = JSON.stringify(data);
        }
        
        try {
            const response = await fetch(url, options);
            const result = await response.json();
            
            if (!response.ok) {
                throw new Error(result.error || 'API 호출 실패');
            }
            
            return result;
        } catch (error) {
            console.error('API Error:', error);
            throw error;
        }
    },
    
    // 날짜 포맷팅
    formatDate(date, format = 'YYYY.MM.DD') {
        const d = new Date(date);
        const year = d.getFullYear();
        const month = String(d.getMonth() + 1).padStart(2, '0');
        const day = String(d.getDate()).padStart(2, '0');
        
        return format
            .replace('YYYY', year)
            .replace('MM', month)
            .replace('DD', day);
    },
    
    // 토스트 알림
    showToast(message, type = 'info') {
        const toastContainer = document.getElementById('toastContainer') || this.createToastContainer();
        
        const toast = document.createElement('div');
        toast.className = `toast align-items-center text-white bg-${type} border-0`;
        toast.setAttribute('role', 'alert');
        toast.innerHTML = `
            <div class="d-flex">
                <div class="toast-body">${message}</div>
                <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button>
            </div>
        `;
        
        toastContainer.appendChild(toast);
        
        const bsToast = new bootstrap.Toast(toast);
        bsToast.show();
        
        // 토스트가 숨겨진 후 DOM에서 제거
        toast.addEventListener('hidden.bs.toast', () => {
            toast.remove();
        });
    },
    
    // 토스트 컨테이너 생성
    createToastContainer() {
        const container = document.createElement('div');
        container.id = 'toastContainer';
        container.className = 'toast-container position-fixed top-0 end-0 p-3';
        container.style.zIndex = '1055';
        document.body.appendChild(container);
        return container;
    },
    
    // 로딩 스피너 표시/숨김
    showLoading(element) {
        const spinner = document.createElement('div');
        spinner.className = 'loading-spinner';
        spinner.id = 'loadingSpinner';
        element.appendChild(spinner);
    },
    
    hideLoading() {
        const spinner = document.getElementById('loadingSpinner');
        if (spinner) {
            spinner.remove();
        }
    },
    
    // 폼 데이터를 객체로 변환
    formToObject(form) {
        const formData = new FormData(form);
        const obj = {};
        for (let [key, value] of formData.entries()) {
            obj[key] = value;
        }
        return obj;
    }
};

// 페이지 로드 시 실행되는 초기화 함수들
document.addEventListener('DOMContentLoaded', function() {
    // Bootstrap 툴팁 초기화
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
    
    // 모든 카드에 hover 효과 추가
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        if (!card.classList.contains('no-hover')) {
            card.addEventListener('mouseenter', function() {
                this.style.transform = 'translateY(-2px)';
                this.style.boxShadow = '0 0.5rem 1rem rgba(0, 0, 0, 0.15)';
            });
            
            card.addEventListener('mouseleave', function() {
                this.style.transform = 'translateY(0)';
                this.style.boxShadow = '0 0.125rem 0.25rem rgba(0, 0, 0, 0.075)';
            });
        }
    });
    
    // 네비게이션 활성 링크 설정
    setActiveNavLink();
    
    // 폼 유효성 검사 개선
    enhanceFormValidation();
});

// 네비게이션 활성 링크 설정
function setActiveNavLink() {
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
    
    navLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (href && currentPath.startsWith(href) && href !== '/') {
            link.classList.add('active');
        } else if (href === '/' && currentPath === '/') {
            link.classList.add('active');
        }
    });
}

// 폼 유효성 검사 개선
function enhanceFormValidation() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        const inputs = form.querySelectorAll('input[required], textarea[required], select[required]');
        
        inputs.forEach(input => {
            input.addEventListener('blur', function() {
                validateField(this);
            });
            
            input.addEventListener('input', function() {
                if (this.classList.contains('is-invalid')) {
                    validateField(this);
                }
            });
        });
    });
}

// 개별 필드 유효성 검사
function validateField(field) {
    const value = field.value.trim();
    const fieldName = field.name;
    let isValid = true;
    let errorMessage = '';
    
    // 필수 필드 검사
    if (field.hasAttribute('required') && !value) {
        isValid = false;
        errorMessage = '이 필드는 필수입니다.';
    }
    
    // 특별한 유효성 검사
    if (value && fieldName === 'email') {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(value)) {
            isValid = false;
            errorMessage = '올바른 이메일 형식이 아닙니다.';
        }
    }
    
    if (value && fieldName === 'username') {
        const usernameRegex = /^[A-Za-z0-9]{4,20}$/;
        if (!usernameRegex.test(value)) {
            isValid = false;
            errorMessage = '아이디는 영문, 숫자 조합 4-20자여야 합니다.';
        }
    }
    
    if (value && fieldName === 'password') {
        const passwordRegex = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$/;
        if (!passwordRegex.test(value)) {
            isValid = false;
            errorMessage = '비밀번호는 영문, 숫자, 특수문자 조합 8자 이상이어야 합니다.';
        }
    }
    
    // UI 업데이트
    const feedbackDiv = field.parentNode.querySelector('.invalid-feedback') || 
                       field.parentNode.querySelector('.valid-feedback');
    
    if (isValid) {
        field.classList.remove('is-invalid');
        field.classList.add('is-valid');
        if (feedbackDiv) {
            feedbackDiv.remove();
        }
    } else {
        field.classList.remove('is-valid');
        field.classList.add('is-invalid');
        
        if (feedbackDiv) {
            feedbackDiv.textContent = errorMessage;
            feedbackDiv.className = 'invalid-feedback';
        } else {
            const newFeedback = document.createElement('div');
            newFeedback.className = 'invalid-feedback';
            newFeedback.textContent = errorMessage;
            field.parentNode.appendChild(newFeedback);
        }
    }
    
    return isValid;
}

// 좋아요 기능
async function toggleLike(type, id) {
    try {
        const result = await Utils.apiCall(`/api/${type}/${id}/like`, 'POST');
        
        // UI 업데이트
        const likeButton = document.querySelector(`[data-${type}-id="${id}"] .like-button`);
        const likeCount = document.querySelector(`[data-${type}-id="${id}"] .like-count`);
        
        if (likeButton && likeCount) {
            const icon = likeButton.querySelector('i');
            if (result.liked) {
                icon.classList.remove('far');
                icon.classList.add('fas');
                likeButton.classList.add('text-danger');
            } else {
                icon.classList.remove('fas');
                icon.classList.add('far');
                likeButton.classList.remove('text-danger');
            }
            
            likeCount.textContent = result.likes;
        }
        
        Utils.showToast(result.message, 'success');
    } catch (error) {
        Utils.showToast('좋아요 처리 중 오류가 발생했습니다.', 'danger');
    }
}

// 이미지 업로드 미리보기
function setupImagePreview(inputId, previewId) {
    const input = document.getElementById(inputId);
    const preview = document.getElementById(previewId);
    
    if (input && preview) {
        input.addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    preview.src = e.target.result;
                    preview.style.display = 'block';
                };
                reader.readAsDataURL(file);
            }
        });
    }
}

// 무한 스크롤 구현
function setupInfiniteScroll(loadMoreFunction) {
    let loading = false;
    
    window.addEventListener('scroll', function() {
        if (loading) return;
        
        if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 1000) {
            loading = true;
            loadMoreFunction().finally(() => {
                loading = false;
            });
        }
    });
}

// 검색 디바운스 함수
function debounce(func, wait) {
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

// 전역 객체로 내보내기
window.PetCare = {
    Utils,
    toggleLike,
    setupImagePreview,
    setupInfiniteScroll,
    debounce,
    validateField
};