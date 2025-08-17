from flask import Blueprint, render_template, request, jsonify

bp = Blueprint('dailycare', __name__)

@bp.route('/')
def index():
    return render_template('dailycare/index.html')

@bp.route('/health')
def health():
    return render_template('dailycare/health.html')

@bp.route('/routine')
def routine():
    return render_template('dailycare/routine.html')

@bp.route('/log', methods=['POST'])
def log_care():
    # TODO: 케어 로그 저장 로직 구현
    return jsonify({'status': 'success', 'message': '케어 기록이 저장되었습니다.'})