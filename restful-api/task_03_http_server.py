from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleAPIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(json.dumps(data).encode())

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(info).encode())

        else:
            self.send_response(404)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

def run():
    port = 8000
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print(f"Server running on http://localhost:{port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
