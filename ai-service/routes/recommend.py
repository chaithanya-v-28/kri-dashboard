from flask import Blueprint, request, jsonify
from services.groq_client import generate_response

recommend_bp = Blueprint("recommend", __name__)

@recommend_bp.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "text required"}), 400

    text = data["text"]

    prompt = f"""
You are a professional risk advisor.

Provide clear, practical, and professional recommendations to mitigate the following risk.

Risk: {text}

Write 3-4 concise recommendations in paragraph form.
Do NOT include instructions or extra text.
"""

    ai_response = generate_response(prompt)

    
    if "AI Insight" in ai_response or not ai_response.strip():
        ai_response = (
            "Organizations should implement strong authentication mechanisms, "
            "regularly update and patch systems, monitor network activity continuously, "
            "and conduct periodic security audits to reduce cybersecurity risks."
        )

    return jsonify({
        "input": text,
        "recommendations": ai_response.strip()
    })