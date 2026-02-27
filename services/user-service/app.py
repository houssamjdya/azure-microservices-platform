import logging
import os
from flask import Flask, jsonify

app = Flask(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)

USERS = [
    {"id": 1, "name": "Alice Hansen", "email": "alice@example.com"},
    {"id": 2, "name": "Bob Nilsen",   "email": "bob@example.com"},
]

@app.route("/health")
def health():
    return jsonify({"status": "healthy", "service": "user-service"}), 200

@app.route("/users")
def get_users():
    logger.info("Fetching all users")
    return jsonify(USERS), 200

@app.route("/users/<int:user_id>")
def get_user(user_id):
    user = next((u for u in USERS if u["id"] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
