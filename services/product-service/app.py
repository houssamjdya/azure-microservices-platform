import logging
import os
import requests
from flask import Flask, jsonify

app = Flask(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)

USER_SERVICE_URL = os.environ.get("USER_SERVICE_URL", "http://user-service:5000")

PRODUCTS = [
    {"id": 1, "name": "Laptop", "price": 9999, "owner_id": 1},
    {"id": 2, "name": "Headphones", "price": 499, "owner_id": 2},
]

@app.route("/health")
def health():
    return jsonify({"status": "healthy", "service": "product-service"}), 200

@app.route("/products")
def get_products():
    logger.info("Fetching all products")
    return jsonify(PRODUCTS), 200

@app.route("/products/<int:product_id>/with-owner")
def get_product_with_owner(product_id):
    product = next((p for p in PRODUCTS if p["id"] == product_id), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    
    try:
        response = requests.get(f"{USER_SERVICE_URL}/users/{product['owner_id']}", timeout=3)
        owner = response.json()
    except requests.exceptions.RequestException as e:
        logger.warning(f"Could not fetch owner: {e}")
        owner = {"error": "User service unavailable"}
    
    return jsonify({**product, "owner": owner}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port)
