from flask import Flask, request
from chatgpt_handler import query_gemini_with_document
from email_sender import send_email
import os

app = Flask(__name__)


@app.route("/ai-webhook", methods=["POST"])
def handle():
    data = request.get_json()
    user_text = data.get("text", "")
    print("Received:", user_text)

    result = query_gemini_with_document(user_text)
    print("Response:", result)

    try:
        send_email(
            recipient=os.getenv("EMAIL_TO"),
            subject="AI Assistant Response",
            body=result
        )
    except Exception as e:
        print("Email failed:", str(e))

    return {"reply": result}


if __name__ == "__main__":
    app.run()
