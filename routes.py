from flask import Flask, jsonify, request, abort

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 1200.00, "availability": True},
]

@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    return jsonify(product) if product else abort(404)

@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if not product:
        abort(404)
    product.update(request.json)
    return jsonify(product)

@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    global products
    products = [p for p in products if p["id"] != product_id]
    return "", 204

@app.route("/products", methods=["GET"])
def list_products():
    name = request.args.get("name")
    category = request.args.get("category")
    availability = request.args.get("availability")

    result = products
    if name:
        result = [p for p in result if p["name"] == name]
    if category:
        result = [p for p in result if p["category"] == category]
    if availability:
        result = [p for p in result if p["availability"] == (availability.lower() == "true")]

    return jsonify(result)
