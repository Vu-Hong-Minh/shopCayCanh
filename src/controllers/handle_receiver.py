from src.models.receiver import get_receiver,get_receiver_by_id,update_receiver,per_page
from flask import Blueprint, request, jsonify


receivers = Blueprint("receivers", __name__)


# lấy danh sách người nhận


@receivers.route("/v1/receivers", methods=['GET'])
def Get_receivers():
    page = request.args.get("page")
    result = get_receiver(page)
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
                "name": i[2],
                "phone": i[3],
                "address": i[4]
            }
            data.append(data1)

        return jsonify({
            'code': 200,
            'data': data,
            'meta': {'page': page, 'per_page': per_page, 'page_url': request.url}
        })


# cập nhật người nhận


@receivers.route('/v1/receivers/<int:id>', methods=['PUT'])
def Update_category(id):
    if get_receiver_by_id(id) == None:
        return jsonify({
            "user-message": "bad-request",
            "internal-message": "Tài nguyên không tồn tại",
            "code": 504
        })

    else:
        try:
            update_receiver(id, request.json['full_name'], request.json['phone'], request.json['address'])
            return jsonify({
                "code": 200,
                "msg": "cập nhật người nhận có id :" + str(id)
            })
        except Exception as e:

            return jsonify({
                "message": "có lỗi xảy ra",
                "error": str(e)})
