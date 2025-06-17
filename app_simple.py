import os
from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-here')

# Initialize SocketIO
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    """Main landing page"""
    return render_template('index.html')

@app.route('/health')
def health_check():
    """Health check endpoint for deployment platforms"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat(),
        'version': '1.0.0',
        'message': 'DebateHub is running successfully!'
    })

@app.route('/app')
def app_main():
    """Main app route"""
    return jsonify({
        'message': 'Welcome to DebateHub!',
        'features': [
            'Real-time debates',
            'User authentication',
            'Netflix-style library',
            'Admin dashboard',
            'Alert system'
        ],
        'status': 'active'
    })

@app.route('/library')
def library():
    """Library route"""
    return jsonify({
        'message': 'DebateHub Library',
        'content': 'Coming soon - Netflix-style content library'
    })

@app.route('/auth/login')
def login():
    """Login route"""
    return jsonify({
        'message': 'Login page',
        'note': 'Authentication system ready for integration'
    })

@app.route('/auth/register')
def register():
    """Register route"""
    return jsonify({
        'message': 'Registration page',
        'note': 'User registration system ready'
    })

# Socket.IO events
@socketio.on('connect')
def on_connect():
    print('Client connected')

@socketio.on('disconnect')
def on_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') != 'production'
    
    if debug:
        socketio.run(app, host='0.0.0.0', port=port, debug=True)
    else:
        socketio.run(app, host='0.0.0.0', port=port, debug=False)
