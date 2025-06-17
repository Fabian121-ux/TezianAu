#!/usr/bin/env python3
"""
Deployment verification script for DebateHub
"""

import os
import sys
import importlib.util

def check_dependencies():
    """Check if all required dependencies can be imported"""
    required_modules = [
        'flask',
        'flask_socketio',
        'supabase',
        'requests'
    ]
    
    missing_modules = []
    
    for module in required_modules:
        try:
            __import__(module)
            print(f"✅ {module} - OK")
        except ImportError:
            missing_modules.append(module)
            print(f"❌ {module} - MISSING")
    
    return len(missing_modules) == 0

def check_environment():
    """Check environment variables"""
    optional_vars = [
        'SUPABASE_URL',
        'SUPABASE_ANON_KEY',
        'SECRET_KEY'
    ]
    
    print("\n🔍 Environment Variables:")
    for var in optional_vars:
        value = os.environ.get(var)
        if value:
            print(f"✅ {var} - SET")
        else:
            print(f"⚠️ {var} - NOT SET (optional)")

def check_app_import():
    """Check if the app can be imported"""
    try:
        from wsgi import app
        print("✅ App import - OK")
        return True
    except Exception as e:
        print(f"❌ App import failed: {e}")
        return False

def main():
    """Main verification function"""
    print("🚀 DebateHub Deployment Verification")
    print("=" * 40)
    
    # Check dependencies
    deps_ok = check_dependencies()
    
    # Check environment
    check_environment()
    
    # Check app import
    app_ok = check_app_import()
    
    print("\n" + "=" * 40)
    if deps_ok and app_ok:
        print("✅ Deployment verification PASSED")
        print("🎯 DebateHub is ready for deployment!")
        return 0
    else:
        print("❌ Deployment verification FAILED")
        print("🔧 Please fix the issues above before deploying")
        return 1

if __name__ == "__main__":
    sys.exit(main())
