import http.server
import os
import pathlib
import socketserver
import time
import webbrowser

ROOT = pathlib.Path(__file__).resolve().parent
os.chdir(ROOT)

PORT = 52341

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def log_message(self, format, *args):
        pass

if __name__ == "__main__":
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
        url = f"http://localhost:{PORT}/?v={int(time.time())}"
        print(f"Serving portfolio at {url}", flush=True)
        try:
            webbrowser.open(url)
        except Exception:
            pass
        httpd.serve_forever()
