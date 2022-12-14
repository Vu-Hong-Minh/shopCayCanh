from datetime import datetime

from flask import Blueprint, request, jsonify

from src.models.gallery import *
from src.models.product import *
from src.models.product_category import *
from src.models.warehouse import insert_warehouse

product = Blueprint("product", __name__)


# sửa sản phẩm


@product.route('/v1/products/<id>', methods=['PUT'])
def Update_product(id):
    if get_category_by_id(id) == None:
        return jsonify({
            "msg": "không tìm thấy sản phẩm",
            "code": 404
        })
    else:
        # try:
        if get_product_by_name(request.json['name']) == None:
            update_at = datetime.now()
            update_product(id,
                           request.json['name'],
                           request.json['science_name'],
                           request.json['price'],
                           request.json['size'],
                           request.json['image'],
                           request.json['uses'],
                           request.json['description'],
                           request.json['care_plant'],
                           request.json['status'],
                           request.json['updated_by'],
                           update_at
                           )
        for item in request.json['category']:
            update_category_id(item['category_id'], item['id'])
        for item in request.json['gallery']:
            update_gallery(item['id'], item['type'], item['url'], )

        return jsonify({
            "code": 0,
            "msg": "cập nhật sản phẩm có id :" + str(id)
        }), 200

    # except Exception as e:
    #
    #     return jsonify({
    #         "message": "có lỗi xảy ra",
    #         "error": str(e)})


# thêm sản phẩm

# thêm sản phẩm list garely ,category , insert bảng kho
@product.route('/v1/products', methods=['POST'])
def create_product():
    if get_product_by_name(request.json['name']) == None:
        create_at = datetime.now()
        sql = insert_product(
            request.json['name'],
            request.json['uses'],
            request.json['science_name'],
            request.json['price'],
            request.json['size'],
            request.json['image'],
            request.json['description'],
            request.json['care_plant'],
            request.json['status'],
            create_at,
            request.json['created_by']


        )
        product_id = int(''.join(map(str, sql)))

        for item in request.json['list_category']:
            insert_product_category(product_id, item)
        for item in request.json['gallery']:
            insert_gallery(product_id, item['type'], item['url'])
        insert_warehouse(product_id, request.json['quantity'])
        return jsonify({
            "message": "tạo sản phẩm thành công",
            "code": 200
        })
    else:
        return jsonify({
            "message": "tên sản phẩm đáuwr dụng , vui lòng đổi tên khác",
            "code": 400
        })


# api lấy danh sách sản phẩm
@product.route('/products', methods=['GET'])
def Get_products():
    page = request.args.get("page")
    result = get_products(page)
    if result == None:
        return jsonify({
            "code": 404,
            "error": "No results found. Check url again",
            "url": request.url
        })
    else:
        data = []

        for i in result:
            created_by = ' '.join([str(get_created_by(i[10]))])
            update_by = get_updated_by(i[12])
            data1 = {
                "id": i[0],
                "name": i[1],
                "science_name": i[2],
                "price": i[3],
                "size": i[4],
                "image": i[5],
                "created_at": i[9],
                "created_by": created_by,
                "updated_at": i[11],
                "updated_by": update_by,
                "status": i[13]

            }
            data.append(data1)

        return jsonify({
            'code': 200,
            'data': data,
            'meta': {'page': page, 'per_page': per_page, 'page_url': request.url}
        })
