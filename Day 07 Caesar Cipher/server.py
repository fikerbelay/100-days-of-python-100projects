import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
from main import caesar, get_cipher_stats


class CaesarHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)

        if parsed_path.path == '/':
            self.serve_file('templates/index.html', 'text/html')
        elif parsed_path.path == '/static/style.css':
            self.serve_file('static/style.css', 'text/css')
        elif parsed_path.path == '/api/test':
            self.send_json({'status': 'API is working!'})
        else:
            self.send_error(404)

    def do_POST(self):
        if self.path == '/api/process':
            self.handle_process()
        else:
            self.send_error(404)

    def serve_file(self, filepath, content_type):
        try:
            with open(filepath, 'r') as f:
                content = f.read()
            self.send_response(200)
            self.send_header('Content-type', content_type)
            self.end_headers()
            self.wfile.write(content.encode())
        except FileNotFoundError:
            self.send_error(404, f'File not found: {filepath}')

    def handle_process(self):
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode())

            text = data.get('text', '').lower()
            shift = int(data.get('shift', 0))
            mode = data.get('mode', 'encode')

            if not text:
                self.send_json({'error': 'Please enter a message'}, 400)
                return

            if shift < 1 or shift > 26:
                self.send_json({'error': 'Shift must be between 1 and 26'}, 400)
                return

            result = caesar(text, shift, mode)
            stats = get_cipher_stats(text, shift, mode)

            self.send_json({
                'success': True,
                'result': result,
                'stats': stats,
                'original': text,
                'mode': mode,
                'shift': shift
            })

        except Exception as e:
            self.send_json({'error': str(e)}, 500)

    def send_json(self, data, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())


def run_server():
    port = 5000
    server = HTTPServer(('', port), CaesarHandler)
    print(f'Server running at http://localhost:{port}')
    print('Press Ctrl+C to stop')
    server.serve_forever()


if __name__ == '__main__':
    run_server()