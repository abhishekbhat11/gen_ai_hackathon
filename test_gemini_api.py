import requests

GEMINI_API_URL = "https://aistudio.google.com/app/apikey"  # Use correct API URL
API_KEY = "AIzaSyAo8qboSblnISY8kcGgrynwGQxbLTd51rE"  # Use correct API key

headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

data = {
    "input": "I am feeling stressed."
}

try:
    response = requests.post(GEMINI_API_URL, headers=headers, json=data)
    response.raise_for_status()
    print(response.json())  # This should print the API response
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
