import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import pyautogui


class Serv(BaseHTTPRequestHandler):
    content = ""
    def do_GET(self):
        # cwd = os.getcwd()
        # print("cwd ", cwd)
        # file_to_open = open("index.html").read()
        self.send_response(200)
        self.end_headers()
        # self.wfile.write(bytes(file_to_open, 'utf-8'))

        if("favicon" not in self.path):
            f = self.path.split(":")
            x=int(f[0][1:])
            y=int(f[1])
            pyautogui.moveTo(x, y, duration=0)


httpd = HTTPServer(('0.0.0.0', 8000), Serv)
httpd.serve_forever()