from datetime import datetime

from flask import Blueprint, request, jsonify

from src.models.detail_receipt import get_detail_receipt, update_detail_receipt, get_total_money, insert_detail_receipt
from src.models.receipt import *
from src.models.warehouse import update_warehouse

receipt = Blueprint("receipt", __name__)


# lấy chi tiết phiếu nhập
@receipt.route('/v1/receipts/<id>/detail', methods=['GET'])
def Get_detail_receipt(id):
    result = get_detail_receipt(id)
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
            'msg': "chi tiết phiếu nhập có id  " + str(id)
        })


# sửa phiếu nhập


@receipt.route('/v1/receipts/<id>', methods=['PUT'])
def Update_receipt(id):
    if get_receipt_by_id(id) == None:
        return jsonify({
            'code': 504,
            'msg': "không tìm thấy phiếu nhập"
        })
    else:
        try:
            updated_at = datetime.now()
            for item in request.json['detail_receipt']:
                update_detail_receipt(item['id'], item['quantity'], item['price'],
                                      int(item['quantity']) * int(item['price']))
            sql = get_total_money(id)
            total_money = int(sql[0])
            update_receipt(id, request.json['updated_by'], updated_at, total_money)

            return jsonify({
                "code": 200,
                "msg": "cập nhật phiếu nhập có id :" + str(id)
            })

        except Exception as e:

            return jsonify({
                "message": "có lỗi xảy ra",
                "error": str(e)})


# thêm phiếu  nhập


@receipt.route('/v1/receipts', methods=['POST'])
def Insert_receipt():
    created_at = datetime.now()
    sql = insert_receipt(request.json['employee_id'], created_at, request.json['total_money'])
    receipt_id = int(''.join(map(str, sql)))
    for item in request.json["detail_receipt"]:
        money = (item['price']) * (item['quantity'])
        insert_detail_receipt(receipt_id, item['product_id'], item['quantity'], item['price'], money)
        update_warehouse(item['product_id'], item['quantity'])
    return jsonify({
        "msg": "tạo thành công phiếu nhập ",
        "code": 201
    })


# lấy danh sách phiếu nhập 
@receipt.route('/v1/receipts',methods = ['GET'])
def Get_receipt():
    page = request.args.get("page")
    result = get_receipt(page)
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
                "category_name": i[1],
                "created_at": i[2],
                "updated_at":i[4],
                "total_money":i[5]
            }
            data.append(data1)

        return jsonify({
            'code': 200,
            'data': data,
            'meta': {'page': page, 'per_page': per_page, 'page_url': request.url}
        })
