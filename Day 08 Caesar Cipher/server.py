import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
from main import caesar, get_cipher_stats


class CaesarHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        print(f"GET: {parsed.path}")

        if parsed.path == '/':
            self.serve_file('templates/index.html', 'text/html')
        elif parsed.path == '/static/style.css':
            self.serve_file('static/style.css', 'text/css')
        elif parsed.path == '/api/test':
            self.send_json({'status': 'API is working!', 'message': 'Server is running'})
        else:
            self.send_error(404)

    def do_POST(self):
        print(f"POST: {self.path}")

        if self.path == '/api/process':
            self.handle_process()
        else:
            self.send_error(404)

    def serve_file(self, path, content_type):
        try:
            with open(path, 'rb') as f:
                content = f.read()
            self.send_response(200)
            self.send_header('Content-type', content_type)
            self.end_headers()
            self.wfile.write(content)
        except FileNotFoundError:
            print(f"File not found: {path}")
            self.send_error(404)

    def handle_process(self):
        try:
            # Read the request body
            length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(length).decode('utf-8')
            data = json.loads(body)

            print(f"Processing: {data}")

            text = data.get('text', '').lower()
            shift = int(data.get('shift', 0))
            mode = data.get('mode', 'encode')

            # Validate
            if not text:
                self.send_json({'error': 'Please enter a message'}, 400)
                return

            if shift < 1 or shift > 26:
                self.send_json({'error': 'Shift must be between 1 and 26'}, 400)
                return

            if mode not in ['encode', 'decode']:
                self.send_json({'error': 'Mode must be "encode" or "decode"'}, 400)
                return

            # Process the cipher
            result = caesar(text, shift, mode)
            stats = get_cipher_stats(text, shift, mode)

            # Send response
            self.send_json({
                'success': True,
                'result': result,
                'stats': stats,
                'original': text,
                'mode': mode,
                'shift': shift
            })

        except json.JSONDecodeError as e:
            print(f"JSON error: {e}")
            self.send_json({'error': 'Invalid JSON format'}, 400)
        except Exception as e:
            print(f"Error: {e}")
            self.send_json({'error': str(e)}, 500)

    def send_json(self, data, status=200):
        response = json.dumps(data)
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Content-Length', str(len(response)))
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))

    def log_message(self, format, *args):
        print(f"[{self.address_string()}] {format % args}")


if __name__ == '__main__':
    port = 5000
    server = HTTPServer(('0.0.0.0', port), CaesarHandler)  # Use 0.0.0.0 to accept all connections
    print(f'=== Caesar Cipher Server ===')
    print(f'Server running at http://localhost:{port}')
    print(f'Also available at http://127.0.0.1:{port}')
    print(f'Press Ctrl+C to stop')
    print(f'============================')
    server.serve_forever()