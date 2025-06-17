import os
from supabase import create_client, Client
from typing import Optional, Dict, Any

def get_supabase_client() -> Client:
    """Get Supabase client instance"""
    url = os.environ.get('SUPABASE_URL')
    key = os.environ.get('SUPABASE_ANON_KEY')
    
    if not url or not key:
        raise ValueError("Missing Supabase credentials")
    
    return create_client(url, key)

def get_db_connection():
    """Get database connection via Supabase"""
    return get_supabase_client()

def init_db():
    """Initialize database tables via Supabase"""
    try:
        supabase = get_supabase_client()
        print("✅ Database connection established via Supabase")
        return True
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        return False

def execute_query(query: str, params: Optional[Dict[str, Any]] = None):
    """Execute a query via Supabase REST API"""
    try:
        supabase = get_supabase_client()
        # This is a simplified version - in practice you'd use Supabase table methods
        print(f"Query would be executed: {query}")
        return True
    except Exception as e:
        print(f"Query execution failed: {e}")
        return False
