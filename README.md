#  KRI Dashboard Backend

---

##  Overview

This project is an AI-powered backend service built using Flask.
It is part of the **KRI (Key Risk Indicator) Dashboard** and provides intelligent risk analysis using AI.

The system processes user inputs and generates:

* Risk descriptions
* Recommendations
* Structured reports
* Document insights
* Batch analysis
* Knowledge retrieval (RAG)

---

##  Features

* 🔹 AI Risk Description
* 🔹 AI Recommendations
* 🔹 Report Generation (Async + Structured Output)
* 🔹 Document Analysis (Insights + Risks)
* 🔹 Batch Processing (Multiple Inputs)
* 🔹 RAG (Retrieval-Augmented Generation using ChromaDB)
* 🔹 Streaming Support (SSE)
* 🔹 Modular Architecture (Routes + Services)

---

## Prerequisites

* Python 3.10+
* pip installed
* Internet connection (for Groq API)
* Git (optional)

---

##  Installation

```bash
git clone https://github.com/chaithanya-v-28/kri-dashboard.git
cd kri-dashboard/ai-service
pip install flask flask-cors python-dotenv requests chromadb sentence-transformers
```

---

##  Environment Variables

Create a `.env` file inside `ai-service`:

```
GROQ_API_KEY=your_groq_api_key_here
```

---

##  Run the Server

```bash
python app.py
```

Server runs at:

```
http://127.0.0.1:5555/
```



##  API Endpoints

---

### 1. Describe Risk

**POST** `/describe`

**Request**

```json
{
  "text": "Cybersecurity risk"
}
```

**Response**

```json
{
  "title": "Cybersecurity Risk",
  "description": "Cybersecurity risks involve threats to systems, networks, and data.",
  "risk_level": "Medium",
  "generated_at": "timestamp"
}
```


### 2. Recommend

**POST** `/recommend`

**Request**

```json
{
  "text": "Cybersecurity risk"
}
```

**Response**

```json
{
  "input": "Cybersecurity risk",
  "recommendations": "Enable multi-factor authentication, update systems regularly, and monitor network activity."
}
```


### 3. Generate Report

**POST** `/generate-report`

**Request**

```json
{
  "text": "Cybersecurity risk"
}
```

**Response**

```json
{
  "title": "Cybersecurity Risk Analysis Report",
  "executive_summary": "...",
  "overview": "...",
  "top_items": [
    "Weak authentication",
    "Unpatched software",
    "Lack of monitoring"
  ],
  "recommendations": [
    {"action": "Enable MFA", "priority": "High"}
  ],
  "generated_at": "timestamp"
}
```


### 4. Analyse Document

**POST** `/analyse-document`

**Request**

```json
{
  "text": "System lacks encryption"
}
```

**Response**

```json
{
  "input": "System lacks encryption",
  "findings": [
    {"type": "insight", "description": "Sensitive data is exposed"},
    {"type": "risk", "description": "High chance of data breach"}
  ],
  "generated_at": "timestamp"
}
```



### 5. Batch Process

**POST** `/batch-process`

**Request**

```json
{
  "items": ["risk1", "risk2"]
}
```

**Response**

```json
{
  "count": 2,
  "results": [
    {"input": "risk1", "output": "..."},
    {"input": "risk2", "output": "..."}
  ]
}
```


### 6. RAG Query

**POST** `/rag`

**Request**

```json
{
  "query": "cybersecurity"
}
```

**Response**

```json
{
  "query": "cybersecurity",
  "results": [
    "Cybersecurity risks include phishing, malware, and data breaches."
  ]
}


## Performance & Optimization

* Preloaded embedding model for faster responses
* Optional Redis caching
* Reduced prompt size for efficiency
* Streaming support for real-time responses


## Testing

Run tests:

bash
pytest


## Status

✔ APIs implemented
✔ Async processing working
✔ Streaming enabled
✔ Batch processing added
✔ Unit tests completed
✔ Demo ready


## Future Improvements

* Add database (PostgreSQL / MongoDB)
* Add authentication (JWT)
* Build React frontend dashboard
* Improve AI prompt quality
* Enable Redis caching fully
* Deploy to cloud (AWS / Render)


## Author

Chaithanya V
AI Developer Intern


## Conclusion

This project demonstrates how AI can be integrated into backend systems to provide real-time risk analysis, intelligent recommendations, and structured reporting.



