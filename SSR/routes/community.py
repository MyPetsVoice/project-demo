from flask import Blueprint, render_template, request, jsonify

bp = Blueprint('community', __name__)

@bp.route('/')
def index():
    return render_template('community/index.html')

@bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        # TODO: 커뮤니티 글 작성 로직 구현
        return jsonify({'status': 'success', 'message': '글이 작성되었습니다.'})
    
    return render_template('community/create.html')

@bp.route('/detail/<int:post_id>')
def detail(post_id):
    # TODO: 커뮤니티 글 상세보기 로직 구현
    return render_template('community/detail.html', post_id=post_id)