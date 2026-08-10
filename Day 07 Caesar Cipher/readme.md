
#  Caesar Cipher Tool

A simple, elegant web application for encrypting and decrypting messages using the Caesar cipher. Built with Python and vanilla JavaScript - no frameworks required!

## Features

- **Encrypt/Decrypt Messages**: Shift letters by any number from 1-26
- **Simple UI**: Clean, responsive interface that works on desktop and mobile
- **Real-time Processing**: Instant results with statistics
- **Copy to Clipboard**: One-click copy of encrypted/decrypted results
- **Keyboard Shortcuts**: Press `Ctrl + Enter` to process messages quickly
- **No External Dependencies**: Pure Python HTTP server, no Flask or other frameworks needed

## Quick Start

### Prerequisites
- Python 3.6 or higher
- A modern web browser (Chrome, Firefox, Edge, Safari)

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/caesar-cipher-tool.git
cd caesar-cipher-tool
```

2. **Run the server:**
```bash
python server.py
```

3. **Open your browser** and navigate to:
```
http://localhost:5000
```

That's it! No additional installation or dependencies required.

##  Project Structure

```
caesar-cipher-tool/
├── server.py          # HTTP server that serves the app
├── main.py            # Caesar cipher logic
├── templates/
│   └── index.html     # Main user interface
└── static/
    └── style.css      # Styling and layout
```

##  How It Works

### The Caesar Cipher
The Caesar cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of positions down the alphabet. For example, with a shift of 3:

- `A` → `D`
- `B` → `E`  
- `C` → `F`

### Using the Tool

1. **Enter your message** in the text area
2. **Choose a mode**:
   - `Encrypt` - Scramble your message
   - `Decrypt` - Unscramble your message
3. **Set the shift amount** (1-26) using the input or +/- buttons
4. **Click "Process Message"** to see the result
5. **Copy the result** with the "Copy Result" button

### Example

**Encrypt:**
- Message: `hello fiker`
- Shift: `3`
- Result: `khoor ilnhu`

**Decrypt:**
- Message: `khoor ilnhu`
- Shift: `3`
- Result: `hello fiker`

##  API Endpoints

The server provides the following API endpoints:

### `GET /api/test`
Tests if the server is running correctly.
```json
{
  "status": "API is working!"
}
```

### `POST /api/process`
Processes a message through the Caesar cipher.
```json
{
  "text": "hello",
  "shift": 3,
  "mode": "encode"
}
```
**Response:**
```json
{
  "success": true,
  "result": "khoor",
  "stats": {
    "original_length": 5,
    "processed_length": 5,
    "shift_used": 3,
    "alphabet_size": 26
  }
}
```

##  Development

### Running in Development Mode
The server runs in debug mode by default. To make changes:

1. Edit any of the Python files
2. The server will automatically restart (if using debug mode)
3. Refresh your browser to see changes

### Adding Features
The code is structured to be easily extendable:

- **Add new cipher algorithms**: Create new functions in `main.py`
- **Modify the UI**: Edit `templates/index.html`
- **Change styling**: Update `static/style.css`
- **Add new API endpoints**: Add routes in `server.py`

## 🧪 Testing

### Test the Server
```bash
curl http://localhost:5000/api/test
```
Expected response: `{"status": "API is working!"}`

### Test the Cipher
```bash
curl -X POST http://localhost:5000/api/process \
  -H "Content-Type: application/json" \
  -d '{"text":"hello","shift":3,"mode":"encode"}'
```

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Works on mobile browsers too!

## Troubleshooting

### CSS Not Loading?
1. Make sure `static/style.css` exists in the correct location
2. Check the browser console (F12) for errors
3. Try refreshing the page with `Ctrl + F5` (hard refresh)

### Server Won't Start?
1. Check if port 5000 is already in use:
   - On Mac/Linux: `lsof -i :5000`
   - On Windows: `netstat -ano | findstr :5000`
2. Change the port in `server.py`:
   ```python
   port = 5001  # Change to any available port
   ```

### "Connection Refused" Error?
1. Make sure the server is running (`python server.py`)
2. Check that you're using `http://localhost:5000` (not `https://`)
3. Check your firewall settings
