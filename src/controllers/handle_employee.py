from src.models.employee import *
from flask import Blueprint, request, jsonify
from datetime import datetime

employees = Blueprint("employees", __name__)


# lấy danh sách nhân viên


@employees.route("/v1/employees", methods=['GET'])
def Get_employees():
    page = request.args.get("page")
    result = get_employee(page)
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
                "full_name": i[2],
                "phone": i[3],
                "date_of_birth": i[4],
                "gender": i[5],
                "address": i[6],
                "job_postion": i[7],
                "created_at": i[9],
                "updated_at": i[10],
                "status": i[11],

            }
            data.append(data1)

        return jsonify({
            'code': 200,
            'data': data,
            'meta': {'page': page, 'per_page': per_page, 'page_url': request.url}
        })
# cập nhật nhân viên


@employees.route('/v1/employees/<int:id>', methods=['PUT'])
def Update_employee(id):

    if get_employee_by_id(id) == None:
        return jsonify({
            "msg": "không tìm thấy nhân viên ",
            "code": 404
        })
    else:
        # try:
        update_at = datetime.now()
        update_employee(id,  request.json['full_name'],
                        request.json['phone'],
                        request.json['date_of_birth'],
                        request.json['gender'],
                        request.json['address'],
                        request.json['job_postion'],
                        request.json['password'],
                        update_at,
                        request.json['status'])

        return jsonify({
            "code": 200,
            "msg": "cập nhật nhân viên có id :" + str(id),

        })
        #
        # except Exception as e:
        #
        #     return jsonify({
        #         "message": "có lỗi xảy ra",
        #         "error": str(e)})


# thêm nhân viên
@employees.route('/v1/employees', methods=['POST'])
def insert_categories():
    if get_employee_by_phone(request.json['phone']) == None:
        created_at = datetime.now()
        insert_employee(request.json['role_id'],
                        request.json['full_name'],
                        request.json['phone'],
                        request.json['date_of_birth'],
                        request.json['gender'],
                        request.json['address'],
                        request.json['job_postion'],
                        request.json['password'],
                        request.json['status'],
                        created_at)
        return jsonify({
            "code": 201,
            "user-message": "tạo mới thành công nhân viên"
        })

    else:
        return jsonify({
            "user-message": "số điện thoại đã sử dụng đã tồn tại",
            "internal-message": "EmployeeIsExits",
            "code": 400
        })
