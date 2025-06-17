import os
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, send_file
from flask_socketio import SocketIO, emit, join_room, leave_room
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import json
from datetime import datetime
import uuid

# Import your modules
from models import User, Debate, Message
from database import get_db_connection, init_db
from supabase_client import get_supabase_client
from alert_system import AlertSystem
from auth import auth_bp
from library import library_bp

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-here')
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB max file size

# Initialize SocketIO
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')

# Initialize Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

# Initialize Alert System
alert_system = AlertSystem()

@login_manager.user_loader
def load_user(user_id):
    try:
        supabase = get_supabase_client()
        result = supabase.table('users').select('*').eq('id', user_id).execute()
        if result.data:
            user_data = result.data[0]
            return User(
                id=user_data['id'],
                username=user_data['username'],
                email=user_data['email'],
                password_hash=user_data['password_hash'],
                is_admin=user_data.get('is_admin', False),
                avatar_url=user_data.get('avatar_url')
            )
    except Exception as e:
        print(f"Error loading user: {e}")
    return None

# Register blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(library_bp, url_prefix='/library')

@app.route('/')
def index():
    try:
        supabase = get_supabase_client()
        
        # Get recent debates
        debates_result = supabase.table('debates').select('*').order('created_at', desc=True).limit(5).execute()
        recent_debates = debates_result.data if debates_result.data else []
        
        # Get user count
        users_result = supabase.table('users').select('id').execute()
        user_count = len(users_result.data) if users_result.data else 0
        
        return render_template('index.html', 
                             recent_debates=recent_debates,
                             user_count=user_count)
    except Exception as e:
        print(f"Error loading index: {e}")
        return render_template('index.html', recent_debates=[], user_count=0)

@app.route('/health')
def health_check():
    """Health check endpoint for deployment platforms"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat(),
        'version': '1.0.0'
    })

# Socket.IO events
@socketio.on('connect')
def on_connect():
    if current_user.is_authenticated:
        print(f'User {current_user.username} connected')
        emit('status', {'msg': f'{current_user.username} has connected'})

@socketio.on('disconnect')
def on_disconnect():
    if current_user.is_authenticated:
        print(f'User {current_user.username} disconnected')

@socketio.on('join_debate')
def on_join_debate(data):
    if current_user.is_authenticated:
        room = data['room']
        join_room(room)
        emit('status', {'msg': f'{current_user.username} joined the debate'}, room=room)

@socketio.on('leave_debate')
def on_leave_debate(data):
    if current_user.is_authenticated:
        room = data['room']
        leave_room(room)
        emit('status', {'msg': f'{current_user.username} left the debate'}, room=room)

@socketio.on('send_message')
def on_send_message(data):
    if current_user.is_authenticated:
        try:
            supabase = get_supabase_client()
            
            # Save message to database
            message_data = {
                'debate_id': data['debate_id'],
                'user_id': current_user.id,
                'content': data['message'],
                'created_at': datetime.utcnow().isoformat()
            }
            
            result = supabase.table('messages').insert(message_data).execute()
            
            if result.data:
                # Emit message to room
                emit('receive_message', {
                    'username': current_user.username,
                    'message': data['message'],
                    'timestamp': datetime.utcnow().strftime('%H:%M:%S'),
                    'avatar_url': current_user.avatar_url
                }, room=data['debate_id'])
                
        except Exception as e:
            print(f"Error sending message: {e}")
            emit('error', {'msg': 'Failed to send message'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') != 'production'
    
    if debug:
        # Development mode
        socketio.run(app, host='0.0.0.0', port=port, debug=True)
    else:
        # Production mode
        socketio.run(app, host='0.0.0.0', port=port, debug=False)
