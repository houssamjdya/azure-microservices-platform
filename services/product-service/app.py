import os
import requests
from flask import Flask, jsonify

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 9999, "owner_id": 1},
    {"id": 2, "name": "Headphones", "price": 499, "owner_id": 2}
]

USER_SERVICE_URL = os.environ.get("USER_SERVICE_URL", "http://user-service:5000")

@app.route('/health')
def health():
    return jsonify({"service": "product-service", "status": "healthy"})

@app.route('/products')
def get_products():
    return jsonify(products)

@app.route('/products/<int:product_id>')
def get_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    try:
        response = requests.get(f"{USER_SERVICE_URL}/users/{product['owner_id']}")
        owner = response.json()
        return jsonify({**product, "owner": owner})
    except:
        return jsonify(product)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
