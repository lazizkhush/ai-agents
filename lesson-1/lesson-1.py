from google import genai
from dotenv import load_dotenv
import json
import requests
import os

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client()
chat = client.chats.create(model="gemini-2.5-flash")

url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"
headers = {
    "x-goog-api-key": API_KEY,
    "Content-Type": "application/json",
}

chat_history = []
with open("history.json", 'r') as file:
    try:
        chat_history.extend(json.load(file))
    except:
        pass

while True:
    user_input = input()
    if user_input.lower() == 'quit':
        break

    chat_history.append({
        "role": "user",
        "parts": [
          {
            "text": user_input
          }
        ]
      })

    response = requests.post(url, headers=headers, json={"contents": chat_history})
    response_text = response.json()["candidates"][0]["content"]["parts"][0]["text"]
    print(response.json())

    chat_history.append({
        "role": "model",
        "parts": [
          {
            "text": response_text
          }
        ]
      })
    
    

with open("history.json", "w") as file:
    json.dump(chat_history, file, indent=4)

