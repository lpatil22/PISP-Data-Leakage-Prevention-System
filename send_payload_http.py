# send_payload_http.py
import requests

URL = "http://localhost:8000"

print("Interactive payload sender. Type 'exit' to quit.")
while True:
    payload = input("Enter payload to send: ")
    if payload.lower() == "exit":
        break
    try:
        response = requests.post(URL, data=payload)
        print(f"[INFO] Server responded: {response.text}")
    except Exception as e:
        print(f"[ERROR] Failed to send payload: {e}")
