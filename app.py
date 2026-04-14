from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 🔹 Universal AI function
def ask_ai(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful AI study assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500
    )
    return response.choices[0].message.content


@app.route("/")
def home():
    return render_template("index.html")


# 🤖 Chat Tutor
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    reply = ask_ai(f"Explain clearly with examples: {user_input}")
    return jsonify({"response": reply})


# 📄 Notes Generator
@app.route("/notes", methods=["POST"])
def notes():
    text = request.json["text"]
    prompt = f"Convert this into short bullet notes with important keywords:\n{text}"
    reply = ask_ai(prompt)
    return jsonify({"response": reply})


# 🧠 Quiz Generator
@app.route("/quiz", methods=["POST"])
def quiz():
    topic = request.json["topic"]
    level = request.json.get("level", "medium")
    
    prompt = f"Create 5 {level} level MCQs with answers on: {topic}"
    reply = ask_ai(prompt)
    return jsonify({"response": reply})


# 📚 Summarizer
@app.route("/summarize", methods=["POST"])
def summarize():
    text = request.json["text"]
    prompt = f"Summarize this and give key points:\n{text}"
    reply = ask_ai(prompt)
    return jsonify({"response": reply})


# 📅 Study Planner
@app.route("/planner", methods=["POST"])
def planner():
    subjects = request.json["subjects"]
    exam_date = request.json["date"]

    prompt = f"""
    Create a daily study timetable for:
    Subjects: {subjects}
    Exam Date: {exam_date}
    Include revision plan.
    """
    reply = ask_ai(prompt)
    return jsonify({"response": reply})


if __name__ == "__main__":
    app.run(debug=True)