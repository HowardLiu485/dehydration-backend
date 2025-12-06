import time
import requests
import random

API_URL = "http://127.0.0.1:5000/predict"

while True:
    mock_data = {
        "hr": random.randint(70, 130),
        "temp": round(random.uniform(35.5, 38.5), 1),
        "activity": random.randint(500, 5000)
    }

    print("Sending:", mock_data)

    try:
        res = requests.post(API_URL, json=mock_data)
        print("Received:", res.json())
    except Exception as e:
        print("Error:", e)

    time.sleep(1)