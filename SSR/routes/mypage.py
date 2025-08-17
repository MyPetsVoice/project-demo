from flask import Blueprint, render_template, request, jsonify

bp = Blueprint('mypage', __name__)

@bp.route('/')
def index():
    return render_template('mypage/index.html')

@bp.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        # TODO: 프로필 업데이트 로직 구현
        return jsonify({'status': 'success', 'message': '프로필이 업데이트되었습니다.'})
    
    return render_template('mypage/profile.html')

@bp.route('/pets')
def pets():
    # TODO: 반려동물 목록 조회 로직 구현
    return render_template('mypage/pets.html')