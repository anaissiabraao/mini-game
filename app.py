from http.server import SimpleHTTPRequestHandler
from wsgiref.simple_server import make_server
from wsgiref.util import setup_testing_defaults
import os
import mimetypes
import posixpath

# Enable CORS for all routes
def add_cors_headers(headers):
    headers.extend([
        ('Access-Control-Allow-Origin', '*'),
        ('Access-Control-Allow-Methods', 'GET, POST, OPTIONS'),
        ('Access-Control-Allow-Headers', 'Content-Type'),
        ('Cache-Control', 'no-store, no-cache, must-revalidate')
    ])
    return headers

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.path.join(os.path.dirname(__file__), 'static'), **kwargs)
    
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        return super().end_headers()

def guess_type(path):
    """Guess the type of a file based on its filename."""
    base, ext = posixpath.splitext(path)
    if ext.lower() == '.js':
        return 'application/javascript'
    elif ext.lower() in ('.html', '.htm'):
        return 'text/html'
    elif ext.lower() == '.css':
        return 'text/css'
    elif ext.lower() in ('.jpg', '.jpeg'):
        return 'image/jpeg'
    elif ext.lower() == '.png':
        return 'image/png'
    elif ext.lower() == '.gif':
        return 'image/gif'
    elif ext.lower() == '.svg':
        return 'image/svg+xml'
    else:
        return 'application/octet-stream'

def simple_app(environ, start_response):
    # Default to index.html for the root path
    path = environ.get('PATH_INFO', '/').lstrip('/')
    if not path:
        path = 'index.html'
    
    # Map path to filesystem
    static_dir = os.path.join(os.path.dirname(__file__), 'static')
    full_path = os.path.normpath(os.path.join(static_dir, path.lstrip('/')))
    
    # Security: Prevent directory traversal
    if not full_path.startswith(static_dir):
        status = '403 Forbidden'
        headers = [('Content-type', 'text/plain')]
        start_response(status, headers)
        return [b'Access denied']
    
    # If path is a directory, look for index.html
    if os.path.isdir(full_path):
        index_path = os.path.join(full_path, 'index.html')
        if os.path.exists(index_path):
            full_path = index_path
        else:
            status = '404 Not Found'
            headers = [('Content-type', 'text/plain')]
            start_response(status, headers)
            return [b'Directory index not found']
    
    # Check if file exists
    if not os.path.isfile(full_path):
        # For SPA routing, serve index.html for any unknown paths
        index_path = os.path.join(static_dir, 'index.html')
        if os.path.exists(index_path):
            full_path = index_path
        else:
            status = '404 Not Found'
            headers = [('Content-type', 'text/plain')]
            start_response(status, headers)
            return [b'File not found']
    
    # Read and serve the file
    try:
        with open(full_path, 'rb') as f:
            content = f.read()
        
        # Determine content type
        content_type = guess_type(path)
        
        status = '200 OK'
        headers = [
            ('Content-type', content_type),
            ('Content-Length', str(len(content))),
            ('Cache-Control', 'no-store, no-cache, must-revalidate'),
            ('Access-Control-Allow-Origin', '*')
        ]
        
        start_response(status, headers)
        return [content]
    except Exception as e:
        status = '500 Internal Server Error'
        headers = [('Content-type', 'text/plain')]
        start_response(status, headers)
        return [str(e).encode('utf-8')]

# WSGI application
def app(environ, start_response):
    # Handle CORS preflight requests
    if environ['REQUEST_METHOD'] == 'OPTIONS':
        headers = [('Content-Type', 'text/plain')]
        headers = add_cors_headers(headers)
        start_response('204 No Content', headers)
        return [b'']
    
    # Handle regular requests
    response_headers = []
    
    try:
        # Get the path from the environment
        path = environ.get('PATH_INFO', '/').lstrip('/')
        if not path:
            path = 'index.html'
            
        # Map path to filesystem
        static_dir = os.path.join(os.path.dirname(__file__), 'static')
        full_path = os.path.normpath(os.path.join(static_dir, path.lstrip('/')))
        
        # Security: Prevent directory traversal
        if not full_path.startswith(static_dir):
            headers = [('Content-Type', 'text/plain')]
            headers = add_cors_headers(headers)
            start_response('403 Forbidden', headers)
            return [b'Access denied']
        
        # If path is a directory, look for index.html
        if os.path.isdir(full_path):
            index_path = os.path.join(full_path, 'index.html')
            if os.path.exists(index_path):
                full_path = index_path
            else:
                headers = [('Content-Type', 'text/plain')]
                headers = add_cors_headers(headers)
                start_response('404 Not Found', headers)
                return [b'Directory index not found']
        
        # Check if file exists
        if not os.path.isfile(full_path):
            # For SPA routing, serve index.html for any unknown paths
            index_path = os.path.join(static_dir, 'index.html')
            if os.path.exists(index_path):
                full_path = index_path
            else:
                headers = [('Content-Type', 'text/plain')]
                headers = add_cors_headers(headers)
                start_response('404 Not Found', headers)
                return [b'File not found']
        
        # Read and serve the file
        with open(full_path, 'rb') as f:
            content = f.read()
        
        # Determine content type
        content_type = guess_type(path)
        
        # Prepare response headers
        headers = [
            ('Content-Type', content_type),
            ('Content-Length', str(len(content)))
        ]
        headers = add_cors_headers(headers)
        
        start_response('200 OK', headers)
        return [content]
        
    except Exception as e:
        headers = [('Content-Type', 'text/plain')]
        headers = add_cors_headers(headers)
        start_response('500 Internal Server Error', headers)
        return [str(e).encode('utf-8')]

# For running locally
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    with make_server('', port, app) as httpd:
        print(f"Starting server on port {port}...")
        print(f"Access the quiz at: http://localhost:{port}")
        print("Press Ctrl+C to stop the server")
        httpd.serve_forever()
