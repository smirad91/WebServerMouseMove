import os
from http.server import HTTPServer, BaseHTTPRequestHandler


class Serv(BaseHTTPRequestHandler):
    content = ""
    def do_GET(self):
        cwd = os.getcwd()
        print("cwd ", cwd)
        file_to_open = open("index.html").read()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))



httpd = HTTPServer(('0.0.0.0', 8080), Serv)
httpd.serve_forever()