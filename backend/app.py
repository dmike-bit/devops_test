import http.server
import socketserver

PORT = 8080

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Hello from Effective Mobile!", PORT)
    httpd.serve_forever()