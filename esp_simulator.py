import requests, time

while True:
    try:
        resp = requests.get("http://127.0.0.1:8000/status/")
        data = resp.json()
        status = data["status"]
        print("💡 Bulb is", "ON" if status else "OFF")
    except Exception as e:
        print("Error:", e)
    time.sleep(2)
