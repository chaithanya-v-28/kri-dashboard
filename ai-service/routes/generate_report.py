from flask import Blueprint, request, jsonify
import threading
import uuid

report_bp = Blueprint("report", __name__)

# Store results
ai_results = {}


def process_async(task_id, text):
    import time
    time.sleep(2)  # simulate processing

    ai_results[task_id] = {
        "title": "Cybersecurity Risk Analysis Report",
        "executive_summary": "Cybersecurity risks can impact systems and data.",
        "overview": "The system may face vulnerabilities like weak authentication and lack of monitoring.",
        "top_items": [
            "Weak authentication",
            "Unpatched software",
            "Lack of monitoring"
        ],
        "recommendations": [
            "Enable multi-factor authentication",
            "Regularly update systems",
            "Monitor network activity"
        ]
    }


@report_bp.route("/generate-report", methods=["POST"])
def generate_report():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "text required"}), 400

    task_id = str(uuid.uuid4())

    thread = threading.Thread(target=process_async, args=(task_id, data["text"]))
    thread.start()

    return jsonify({
        "task_id": task_id,
        "status": "processing"
    })


@report_bp.route("/report-result/<task_id>", methods=["GET"])
def get_report_result(task_id):
    if task_id in ai_results:
        return jsonify({
            "status": "completed",
            "result": ai_results[task_id]
        })
    else:
        return jsonify({"status": "processing"})