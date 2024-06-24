import requests
import time

grafana_url = "http://localhost:3000/api/alertmanager/grafana/api/v1/silence"
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer glsa_IgM6aFvHhaSV0gApkxWqU8M4pUZU0pAi_b6fcc116'
}
initial_interval = 300  # 5 minutes
max_interval = 43200  # 12 hours

current_interval = initial_interval

while True:
    silence = {
        "matchers": [
            {
                "name": "alertname",
                "value": "HighErrorRate",
                "isRegex": False
            }
        ],
        "startsAt": time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
        "endsAt": time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(time.time() + current_interval)),
        "createdBy": "script",
        "comment": "Exponential backoff for HighErrorRate alert"
    }

    response = requests.post(grafana_url, json=silence, headers=headers)
    if response.status_code == 200:
        print(f"Created silence for {current_interval} seconds")
    else:
        print(f"Failed to create silence: {response.text}")

    time.sleep(current_interval)

    # Exponential backoff
    current_interval = min(current_interval * 2, max_interval)
