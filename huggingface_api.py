import requests

API_URL = "https://api-inference.huggingface.co/models/facebook/llama-2-7b"
API_TOKEN = "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"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def ask_fingpt(prompt):
    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
    if response.status_code == 200:
        result = response.json()
        return result[0]["generated_text"] if "generated_text" in result[0] else "No valid response."
    else:
        return f"Error: {response.text}"
