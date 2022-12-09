from src.models.product import *
from flask import Blueprint, request, jsonify

product = Blueprint("product", __name__)

@product.route("/v1/products")
def get_products_by_category():
    data = request.json
    category_id =int(data.get('category_id'))
    result = get_product_category(category_id)
    data = []
    for i in result:
        data1 = {
            "product_id": i[1],
            "product_name": i[2]
        }
        data.append(data1)
    return jsonify({
        "code": 200,
        "data": data
    })
