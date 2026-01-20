import http.server
import socketserver
import os

PORT = int(os.environ.get("PORT", 8000))

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Servindo na porta {PORT}")
    httpd.serve_forever()
