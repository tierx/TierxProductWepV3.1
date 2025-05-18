import http.server
import threading
import os

def start_web_server():
    """เริ่มเว็บเซิร์ฟเวอร์อย่างง่ายสำหรับ Render.com
    เพื่อให้ Render.com สามารถตรวจพบพอร์ตที่กำลังทำงาน"""
    
    class Handler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><head><title>Discord Bot</title></head><body><h1>Discord Shop Bot</h1><p>Bot is running!</p></body></html>')
    
    server_address = ('0.0.0.0', 8080)  # Render.com expects a port to be open
    httpd = http.server.HTTPServer(server_address, Handler)
    print("Starting web server on port 8080 for Render.com")
    httpd.serve_forever()

def start_server_in_thread():
    """เริ่มเซิร์ฟเวอร์ในเธรดแยก"""
    # Run only if RENDER environment variable is set (on Render.com)
    if os.environ.get("RENDER"):
        threading.Thread(target=start_web_server, daemon=True).start()
        print("Web server thread started for Render.com")