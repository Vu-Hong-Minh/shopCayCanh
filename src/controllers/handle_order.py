from src.models.detail_order import *
from src.models.order import *
from flask import Blueprint, request, jsonify
from datetime import datetime

orders = Blueprint("orders", __name__)

# lấy chi tiest dơn hàng của đơn hàng :

@orders.route('/v1/orders/<id>/detail', methods=['GET'])
def Get_detail_order(id):
    result = get_detail_order(id)
    if result == None:
        return jsonify({
            "code": 404,
            "error": "No results found. Check url again",
            "url": request.url
        })
    else:
        data = []
        for i in result:
            money = int(i[2]) * int(i[3])
            data1 = {
                "id": i[1],
                "full_name": i[0],
                "quantity": i[2],
                "price": i[3],
                "money": money
            }
            data.append(data1)

        return jsonify({
            'code': 200,
            'data': data,
            'msg': "chi tiết đơn hàng có id  " + str(id)
        })


# sửa đơn hàng


@orders.route('/v1/orders/<id>', methods=['PUT'])
def Update_receipt(id):
    if get_order_by_id(id) == None:
        return jsonify({
            'code': 504,
            'msg': "không tìm thấy đơn hàng"
        })
    else:
        # try:
            updated_at = datetime.now()
            for item in request.json['detail_order']:
                update_detail_order(item['id'], item['quantity'], item['price'],
                                      int(item['quantity']) * int(item['price']))
            sql = get_total_money(id)
            total_money = int(sql[0])
            update_order(id, request.json['updated_by'], updated_at, total_money,request.json['status'])

            return jsonify({
                "code": 200,
                "msg": "cập nhật phiếu nhập có id :" + str(id)
            })

        # except Exception as e:
        #
        #     return jsonify({
        #         "message": "có lỗi xảy ra",
        #         "error": str(e)})
