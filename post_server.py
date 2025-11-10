# post_server.py
from http.server import HTTPServer, BaseHTTPRequestHandler
from network_dlp import analyze_payload, load_rules, mask_sensitive_data

HOST = "localhost"
PORT = 8000

class DLPHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')

        rules = load_rules()
        sensitive_detected = analyze_payload(post_data, rules)

        if sensitive_detected and rules.get("block_sensitive", True):
            masked_data = mask_sensitive_data(post_data, rules)
            print(f"[INFO] Received POST: {masked_data}")
            result = "BLOCKED"
            print(f"[INFO] Server responded: BLOCKED")
        else:
            # No sensitive data found, show original payload
            print(f"[INFO] Received POST: {post_data}")
            result = "ALLOWED"
            print(f"[INFO] Server responded: ALLOWED")

        # Send response
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(result.encode('utf-8'))

def run_server():
    server_address = (HOST, PORT)
    httpd = HTTPServer(server_address, DLPHandler)
    print(f"[INFO] Starting POST server at http://{HOST}:{PORT}")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
