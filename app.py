# Flask Backend Starter for Cloud Sync
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/health")
def health():
    return jsonify({"status": "ok", "ide": "NovaCode Studio"})

if __name__ == "__main__":
    print("Flask server ready on http://localhost:5000")