from src.models.category import *
from src.models.product_category import update_product_id, insert_product_category
from flask import Blueprint, request, jsonify

categories = Blueprint("categories", __name__)

# lấy danh sách danh mục


@categories.route("/v1/categories", methods=['GET'])
def Get_categories():
    page = request.args.get("page")
    result = get_category(page)
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
                "category_id": i[0],
                "category_name": i[1],
                "status": i[2]
            }
            data.append(data1)

        return jsonify({
            'code': 200,
            'data': data,
            'meta': {'page': page, 'per_page': per_page, 'page_url': request.url}
        })
# cập nhật danh mục


@categories.route('/v1/categories/<int:id>', methods=['PUT'])
def Update_category(id):
    if len(get_category_by_id(id)) != 0:
        if get_category_by_name(request.json['name']) == None:
            try:
                update_category(
                    id, request.json['name'], request.json['status'])
                for item in request.json['list_product']:
                    update_product_id(item['product_id'], item['id'])

                return jsonify({
                    "code": 200,
                    "msg": "cập nhật danh mục có id :" + str(id),

                })

            except Exception as e:

                return jsonify({
                    "message": "có lỗi xảy ra",
                    "error": str(e)})

        else:
            return jsonify({
                "msg": "tên danh mục đã tồn tại vui lòng chọn tên khác",
                "code": 400
            })

    else:
        return "không tìm được id "


# thêm danh mục
@categories.route('/v1/categories', methods=['POST'])
def insert_categories():
    if get_category_by_name(request.json['name']) == None:
        sql = insert_category(request.json['name'], request.json['status'])
        category_id = int(''.join(map(str, sql)))
        for item in request.json['product_id']:
            insert_product_category(item, category_id)
        return jsonify({
            "code": 201,
            "user-message": "tạo danh mục thành công"
        })

    else:
        return jsonify({
            "user-message": "tên danh mục đã tồn tại",
            "internal-message": "CategoryIsExits",
            "code": 400
        })
