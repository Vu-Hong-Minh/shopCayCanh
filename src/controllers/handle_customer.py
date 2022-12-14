from src.models.customer import *
from flask import Blueprint, request, jsonify
from datetime import datetime

customers = Blueprint("customers", __name__)

# lấy danh sách khách hàng


@customers.route("/v1/customers", methods=['GET'])
def Get_customers():
    page = request.args.get("page")
    result = get_customer(page)
    if result == None:
        return jsonify({
            "code": 404,
            "error": "No results found. Check url again",
            "url": request.url
        })
    else:
        data = []
        for i in result:
            data1 = {
                "id": i[0],
                "name": i[1],
                "gender": i[2],
                "email": i[3],
                "phone": i[4],
                "address": i[5],
                "created_at": i[7],
                "updated_at": i[8],
                "updated_by": i[9]
            }
            data.append(data1)

        return jsonify({
            'code': 200,
            'data': data,
            'meta': {'page': page, 'per_page': per_page, 'page_url': request.url}
        })

# cập nhật khách hàng


@customers.route('/v1/customers/<int:id>', methods=['PUT'])
def Update_category(id):
    if get_customer_by_id(id) == None:
        return jsonify({
            "user-message": "bad-request",
            "internal-message": "Tài nguyên không tồn tại",
            "code": 504
        })

    else:
        try:
            update_at = datetime.now()
            update_customer(id, request.json['full_name'], request.json['gender'], request.json['email'],
                            request.json['phone'], request.json['address'], update_at, request.json['updated_by'])
            return jsonify({
                "code": 200,
                "msg": "cập nhật khách hàng có id :" + str(id)
            })
        except Exception as e:

            return jsonify({
                "message": "có lỗi xảy ra",
                "error": str(e)})
