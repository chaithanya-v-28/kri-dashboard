from flask import Blueprint, request, jsonify
from services.groq_client import generate_response
from datetime import datetime
import json

describe_bp = Blueprint("describe", __name__)

@describe_bp.route("/describe", methods=["POST"])
def describe():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "text required"}), 400

    text = data["text"]

    prompt = f"""
You are a professional risk analyst.

Analyze the given risk and return ONLY valid JSON.

Risk: {text}

Return format:
{{
  "title": "Short professional title",
  "description": "Clear explanation",
  "risk_level": "Low/Medium/High"
}}
"""

    ai_response = generate_response(prompt)

    
    try:
        parsed = json.loads(ai_response)
    except:
        
        parsed = {
            "title": text,
            "description": f"{text} may impact system security and operations.",
            "risk_level": "Medium"
        }

    parsed["generated_at"] = datetime.utcnow().isoformat()

    return jsonify(parsed)