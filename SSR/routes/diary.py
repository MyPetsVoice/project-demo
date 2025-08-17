from flask import Blueprint, render_template, request, jsonify

bp = Blueprint('diary', __name__)

@bp.route('/')
def index():
    return render_template('diary/index.html')

@bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        # TODO: 일기 생성 로직 구현
        return jsonify({'status': 'success', 'message': '일기가 작성되었습니다.'})
    
    return render_template('diary/create.html')

@bp.route('/detail/<int:diary_id>')
def detail(diary_id):
    # TODO: 일기 상세보기 로직 구현
    return render_template('diary/detail.html', diary_id=diary_id)