import requests
import json

url = "http://localhost:11434/api/generate"

headers = {
    "Content-Type": "application/json"
}

data = {
    "model": "llama2",
    "prompt": "Why is the sky blue?",
    "Stream": False
}

response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    response_text = response.text
    data = json.loads(response_text)
    actual_response = data["response"]
    print(actual_response)
else:
    print("Error:", response.status_code, response.text)
