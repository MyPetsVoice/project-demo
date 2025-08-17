#!/usr/bin/env python3
"""
간단한 테스트 서버 - 기본 연결 확인용
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def test():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>PetCare 테스트</title>
        <meta charset="UTF-8">
    </head>
    <body>
        <h1>🎉 PetCare 테스트 서버 작동 중!</h1>
        <p>이 페이지가 보인다면 Flask 서버가 정상적으로 실행되고 있습니다.</p>
        <p>이제 메인 서버를 실행해보세요.</p>
        <hr>
        <p><strong>다음 단계:</strong></p>
        <ol>
            <li>이 테스트 서버를 종료하세요 (Ctrl+C)</li>
            <li><code>python simple_start.py</code> 실행</li>
        </ol>
    </body>
    </html>
    '''

@app.route('/health')
def health():
    return {'status': 'OK', 'message': 'Server is running'}

if __name__ == '__main__':
    print("🧪 테스트 서버 시작...")
    print("📍 브라우저에서 http://localhost:5001 접속해보세요")
    print("✅ 이 페이지가 열리면 Flask가 정상 작동하는 것입니다")
    
    app.run(debug=True, host='127.0.0.1', port=5001)