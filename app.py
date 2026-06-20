import os
import traceback
from datetime import datetime

from flask import Flask
from flask import jsonify
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for

from src.rag import rag

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "studymate-dev-secret-key")


def _timestamp():
    return datetime.now().strftime("%I:%M %p")


def _chat_history():
    if "chat_history" not in session:
        session["chat_history"] = [
            {
                "role": "assistant",
                "content": "Hi, I am StudyMate AI. Ask a question from your notes and I will answer with sources.",
                "sources": [],
                "timestamp": _timestamp(),
            }
        ]

    return session["chat_history"]


def _append_message(role, content, sources=None):
    history = _chat_history()
    history.append(
        {
            "role": role,
            "content": content,
            "sources": sources or [],
            "timestamp": _timestamp(),
        }
    )
    session["chat_history"] = history
    session.modified = True


def _history_text():
    return "\n".join(
        f"{message.get('role', 'unknown')}: {message.get('content', '')}"
        for message in _chat_history()
        if isinstance(message, dict)
    )


def _answer_query(query, history):
    answer, sources = rag(
        query,
        history
    )

    return answer, sources

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        query = request.form.get("query", "").strip()

        if query:
            history = _history_text()
            _append_message("user", query)
            answer, sources = _answer_query(query, history)
            _append_message("assistant", answer, sources)

        return redirect(url_for("home"))

    return render_template("index.html", messages=_chat_history())


@app.route("/chat", methods=["POST"])
def chat():
    try:
        payload = request.get_json(silent=True) or {}
        query = payload.get("query", "").strip()

        if not query:
            return jsonify({"error": "Please enter a question."}), 400

        history = _history_text()
        _append_message("user", query)

        answer, sources = _answer_query(query, history)

        _append_message("assistant", answer, sources)

        return jsonify(
            {
                "answer": answer,
                "sources": sources,
                "messages": session["chat_history"],
            }
        )
    except Exception as error:
        traceback.print_exc()
        return jsonify({"error": str(error)}), 500


@app.route("/clear", methods=["POST"])
def clear_chat():
    session.pop("chat_history", None)
    _chat_history()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
