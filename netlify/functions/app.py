import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from app import app

def handler(event, context):
    """Netlify function handler"""
    try:
        # Import the WSGI adapter
        from werkzeug.serving import WSGIRequestHandler
        from werkzeug.wrappers import Request, Response
        
        # Create a request from the event
        environ = {
            'REQUEST_METHOD': event.get('httpMethod', 'GET'),
            'PATH_INFO': event.get('path', '/'),
            'QUERY_STRING': event.get('queryStringParameters', ''),
            'CONTENT_TYPE': event.get('headers', {}).get('content-type', ''),
            'CONTENT_LENGTH': str(len(event.get('body', ''))),
            'HTTP_HOST': event.get('headers', {}).get('host', 'localhost'),
            'wsgi.input': event.get('body', ''),
            'wsgi.errors': sys.stderr,
        }
        
        # Add headers to environ
        for key, value in event.get('headers', {}).items():
            key = 'HTTP_' + key.upper().replace('-', '_')
            environ[key] = value
        
        # Call the Flask app
        response = Response.from_app(app, environ)
        
        return {
            'statusCode': response.status_code,
            'headers': dict(response.headers),
            'body': response.get_data(as_text=True)
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error: {str(e)}'
        }
