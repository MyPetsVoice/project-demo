from flask import Blueprint, render_template, request, jsonify

bp = Blueprint('chat', __name__)

@bp.route('/')
def index():
    return render_template('chat/index.html')

@bp.route('/send', methods=['POST'])
def send_message():
    data = request.get_json()
    message = data.get('message', '')
    
    # TODO: AI 챗봇 로직 구현
    response = {
        'response': f"반려동물이 말합니다: {message}에 대한 답변입니다.",
        'status': 'success'
    }
    
    return jsonify(response)