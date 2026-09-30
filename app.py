
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from groq import Groq
import os
from pathlib import Path

env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY not found in.env - get free key at console.groq.com/keys")

app = Flask(__name__)
client = Groq(api_key=api_key)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"error": "No message"}), 400

    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b", # FREE and very smart
            messages=[
                {"role": "system", "content": "You are a helpful customer support assistant. Be friendly and concise."},
                {"role": "user", "content": user_message}
            ]
        )
        reply = response.choices[0].message.content
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)