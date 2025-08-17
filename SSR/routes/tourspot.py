from flask import Blueprint, render_template, request, jsonify

bp = Blueprint('tourspot', __name__)

@bp.route('/')
def index():
    return render_template('tourspot/index.html')

@bp.route('/recommendations')
def recommendations():
    # TODO: 투어스팟 추천 로직 구현
    return jsonify({'status': 'success', 'spots': []})