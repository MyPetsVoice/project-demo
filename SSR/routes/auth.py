from flask import Blueprint, render_template, request, redirect, url_for, session, flash

bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # TODO: 실제 인증 로직 구현
        if username and password:
            session['user_id'] = username
            session['user_name'] = username
            flash('로그인 성공!', 'success')
            return redirect(url_for('chat.index'))
        else:
            flash('로그인 정보를 확인해주세요.', 'error')
    
    return render_template('auth/login.html')

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # TODO: 회원가입 로직 구현
        flash('회원가입이 완료되었습니다.', 'success')
        return redirect(url_for('auth.login'))
    
    return render_template('auth/signup.html')

@bp.route('/logout')
def logout():
    session.clear()
    flash('로그아웃되었습니다.', 'info')
    return redirect(url_for('chat.index'))