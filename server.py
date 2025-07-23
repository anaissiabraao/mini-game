from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.path.join(os.path.dirname(__file__), 'static'), **kwargs)
    
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        return super().end_headers()

def run(server_class=HTTPServer, handler_class=CORSRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    print(f"Access the quiz at: http://localhost:{port}")
    print("Press Ctrl+C to stop the server")
    print("\nIf you can't access the page, please check:")
    print("1. Your firewall settings")
    print("2. If another program is using port 8080")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
