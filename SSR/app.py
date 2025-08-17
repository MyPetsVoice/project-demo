from flask import Flask, render_template, redirect, url_for
from routes import auth, chat, diary, community, place, tourspot, dailycare, mypage

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    # 블루프린트 등록
    app.register_blueprint(auth.bp, url_prefix='/auth')
    app.register_blueprint(chat.bp, url_prefix='/chat')
    app.register_blueprint(diary.bp, url_prefix='/diary')
    app.register_blueprint(community.bp, url_prefix='/community')
    app.register_blueprint(place.bp, url_prefix='/place')
    app.register_blueprint(tourspot.bp, url_prefix='/tourspot')
    app.register_blueprint(dailycare.bp, url_prefix='/dailycare')
    app.register_blueprint(mypage.bp, url_prefix='/mypage')
    
    @app.route('/')
    def index():
        return redirect(url_for('chat.index'))
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)