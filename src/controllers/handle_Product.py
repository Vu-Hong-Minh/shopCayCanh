from src.models.product import *
from src.models.gallery import *
from math import ceil
from flask import Blueprint, request, jsonify

product = Blueprint("product", __name__)

#Api Lấy danh sách sản phẩm theo danh mục
@product.route("/v1/products", methods=['GET'])
def get_products_by_category():
    data = request.json
    page_number = request.args.get("page", default=1, type=int)
    size = request.args.get("size", default=12, type=int)
    if page_number == 2:
        start_record = size
    else:
        start_record = (page_number * size) - size
    if page_number == 1:
        limit = 'limit {}'.format(size)
    else:
        limit = 'limit {}, {}'.format(start_record, size)
    category_id =int(data.get('category_id'))
    sql = "select Table1.name, product.id, product.name from product inner join(select category.name, product_category.product_id from category inner join product_category ON category.id = {} and category.id = product_category.category_id) as Table1 ON Table1.product_id = product.id ".format(
        category_id) + limit
    result = get_data_products(sql)
    sql1 = "select Table1.name, product.id, product.name from product inner join(select category.name, product_category.product_id from category inner join product_category ON category.id = {} and category.id = product_category.category_id) as Table1 ON Table1.product_id = product.id ".format(
        category_id)
    result1 = get_data_products(sql1)
    if len(result1) < size:
        total_page = 1
    else:
        total_page = ceil(len(result1) / size)
    data = [
        {
            "total_page": total_page
        }
    ]
    for i in result:
        data1 = {
            "product_id": i[1],
            "product_name": i[2]
        }
        data.append(data1)
    return jsonify({
        "code": 200,
        "data": data,
        "internal_message": "Request thành công"
    })

#Api lấy thông tin chi tiết sản phẩm
@product.route("/v1/products/<int:product_id>", methods=['GET'])
def get_product_details(product_id):
    sql = "Select * from product where id = {}".format(product_id)
    result = get_data_product(sql)
    sql1 = "Select * from gallery where product_id = {}".format(product_id)
    result1 = get_data_galleries(sql1)
    product_thumnail = {}
    for i in result1:
        product_thumnail_detail = {
            i[0]: {
                "ID": i[0],
                "type": i[2],
                "url": i[3]
            }
        }
        product_thumnail.update(product_thumnail_detail)
    data = {
        "product_name": result[1],
        "product_science_name": result[2],
        "product_price": result[3],
        "product_size": result[4],
        "product_uses": result[6],
        "product_description": result[7],
        "product_care_plant": result[8],
        "product_image": result[5],
        "product_thumnail": product_thumnail
    }
    return jsonify({
        "code": 200,
        "data": data,
        "internal_message": "Request thành công"
    })

#Api tìm kiếm sản phẩm
@product.route("/v1/products/search", methods=['GET'])
def search_product():
    query = request.args.get("q", type=str)
    page_number = request.args.get("page", default=1, type=int)
    size = request.args.get("size", default=12, type=int)
    if page_number == 2:
        start_record = size
    else:
        start_record = (page_number * size) - size
    if page_number == 1:
        limit = 'limit {}'.format(size)
    else:
        limit = 'limit {}, {}'.format(start_record, size)
    sql = "Select id, name, price from product where name like \'%{}%\'".format(query) + limit
    result = get_data_products(sql)
    sql1 = "select id from product where name like\'%{}%\'".format(query)
    result1 = get_data_products(sql1)
    print(len(result1))
    if len(result1) < size:
        total_page = 1
    else:
        total_page = ceil(len(result1) / size)
    data = [
        {
            "total_page": total_page
        }
    ]
    #lặp lấy dữ liệu sản phẩm trong mảng lấy ra
    for i in result:
        temp = {
            "product_id": i[0],
            "product_name": i[1],
            "product_price": i[2]
        }
        data.append(temp)
    return jsonify({
        "code": 200,
        "data": data,
        "internal_message": "Request thành công"
    })