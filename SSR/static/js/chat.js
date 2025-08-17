class ChatManager {
    constructor() {
        this.init();
    }
    
    init() {
        this.setupEventListeners();
    }
    
    setupEventListeners() {
        const chatInput = document.getElementById('chat-input');
        const sendBtn = document.getElementById('chat-send-btn');
        
        if (chatInput) {
            chatInput.addEventListener('keypress', (e) => {
                if (e.key === 'Enter') {
                    this.sendMessage();
                }
            });
        }
        
        if (sendBtn) {
            sendBtn.addEventListener('click', () => {
                this.sendMessage();
            });
        }
    }
    
    async sendMessage() {
        const chatInput = document.getElementById('chat-input');
        const message = chatInput.value.trim();
        
        if (!message) return;
        
        try {
            const response = await fetch('/chat/send', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message })
            });
            
            const data = await response.json();
            
            if (data.status === 'success') {
                this.addMessageToChat(message, 'user');
                this.addMessageToChat(data.response, 'bot');
                chatInput.value = '';
            }
        } catch (error) {
            CommonUtils.showToast('메시지 전송에 실패했습니다.', 'error');
        }
    }
    
    addMessageToChat(message, sender) {
        const chatMessages = document.getElementById('chat-messages');
        const messageElement = document.createElement('div');
        messageElement.className = `message ${sender}`;
        messageElement.textContent = message;
        chatMessages.appendChild(messageElement);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
    
    selectChatPet() {
        const select = document.getElementById('chat-pet-select');
        const selectedPet = select.value;
        
        if (selectedPet) {
            const chatMessages = document.getElementById('chat-messages');
            chatMessages.innerHTML = `
                <div style="text-align: center; padding: 40px; color: #666;">
                    <div style="font-size: 48px; margin-bottom: 20px;">🐾</div>
                    <p>${select.options[select.selectedIndex].text}와의 대화를 시작합니다!</p>
                </div>
            `;
        }
    }
}

window.selectChatPet = function() {
    if (window.chatManager) {
        window.chatManager.selectChatPet();
    }
};

window.handleChatKeyPress = function(event) {
    if (event.key === 'Enter' && window.chatManager) {
        window.chatManager.sendMessage();
    }
};

window.sendMessage = function() {
    if (window.chatManager) {
        window.chatManager.sendMessage();
    }
};

document.addEventListener('DOMContentLoaded', () => {
    window.chatManager = new ChatManager();
});