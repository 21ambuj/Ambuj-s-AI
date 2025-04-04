from flask import Flask, request
import requests

app = Flask(__name__)

# 🔐 Replace with your actual Groq API key
GROQ_API_KEY = "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"

def get_response_from_groq(user_input):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant that helps users with networking assistance."},
            {"role": "user", "content": user_input}
        ],
        "model": "llama3-8b-8192",
    }

    response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data)
    return response.json()['choices'][0]['message']['content']

@app.route("/")
def home():
    return ("index.html")

@app.route("/get", methods=["GET"])
def get_bot_response():
    user_input = request.args.get("msg")
    response = get_response_from_groq(user_input)
    return response

if __name__ == "__main__":
    app.run(debug=True)
