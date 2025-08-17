from flask import Blueprint, render_template, request, jsonify

bp = Blueprint('place', __name__)

@bp.route('/')
def index():
    return render_template('place/index.html')

@bp.route('/search')
def search():
    # TODO: 장소 검색 로직 구현
    query = request.args.get('q', '')
    return jsonify({'status': 'success', 'places': []})