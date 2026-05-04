from flask import Blueprint, request, jsonify
import chromadb
from chromadb.utils import embedding_functions

rag_bp = Blueprint("rag", __name__)

embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="kri_docs",
    embedding_function=embedding_function
)

@rag_bp.route("/rag", methods=["POST"])
def rag_query():
    data = request.get_json()

    if not data or "query" not in data:
        return jsonify({"error": "query required"}), 400

    query = data["query"]

    results = collection.query(
        query_texts=[query],
        n_results=2
    )

    return jsonify({
        "query": query,
        "results": results["documents"][0]
    })