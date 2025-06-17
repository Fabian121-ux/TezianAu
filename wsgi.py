import os
import sys

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(__file__))

try:
    # Try to import the full app first
    from app import app, socketio
    print("✅ Full app loaded successfully")
except ImportError as e:
    print(f"⚠️ Full app failed to load: {e}")
    print("🔄 Loading simplified app...")
    # Fallback to simplified app
    from app_simple import app, socketio
    print("✅ Simplified app loaded successfully")

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    socketio.run(app, host='0.0.0.0', port=port, debug=False)
