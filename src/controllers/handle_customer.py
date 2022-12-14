from socket import gaierror

from src.models.customer import *
from flask import Blueprint, request, jsonify
from datetime import datetime
from src.models.manager_code import *
import random
import smtplib


customer = Blueprint("customer", __name__)

#Api đăng nhập
@customer.route("/v1/login", methods=['POST'])
def login():
    data = request.json
    customer_email = data.get('customer_email')
    customer_pass = data.get('customer_password')
    sql = 'Select * from customer where email = \'{}\''.format(customer_email)
    check = get_data_customer(sql)
    if check != None:
        if customer_pass == check[6]:
            return jsonify({
                "code": 200,
                "user_message": "Đăng nhập thành công",
                "internal_message": "Request thành công"
            })
        else:
            return jsonify({
                "code": 200,
                "user_message": "Sai mật khẩu",
                "internal_message": "Request thành công"
            })
    else:
        return jsonify({
            "code": 200,
            "user_message": "Tài khoản không tồn tại",
            "internal_messager": "Request"
        })

#Api đăng ký
@customer.route("/v1/register", methods=['POST'])
def register():
    data = request.json
    full_name = data.get('full_name')
    customer_gender = data.get('customer_gender')
    customer_phone = data.get('customer_phone')
    customer_email = data.get('customer_email')
    customer_address = data.get('customer_address')
    customer_password = data.get('customer_password')
    now_time = datetime.now()
    sql1 = 'Select * from customer where email = \'{}\''.format(customer_email)
    check = get_data_customer(sql1)
    if check != None:
        return jsonify({
            "code": 200,
            "user_message": "Email đã tồn tại",
            "internal_message": "Request thành công"
        })
    else:
        sql = "insert into customer(full_name, gender, email, phone, address, password, created_at) values (\'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\')".format(
            full_name, customer_gender, customer_email, customer_phone, customer_address, customer_password, now_time)
        update_customer(sql)
        check1 = get_data_customer(sql1)
        if check1 != None:
            return jsonify({
                "code": 200,
                "user_message": "Đăng ký tài khoản thành công",
                "internal_message": "Request thành công"
            })
        else:
            return jsonify({
                "internal_message": "Có lỗi khi thêm tài khoản vào CSDL"
            })

#Api đổi mật khẩu
@customer.route("/v1/customers/<int:customer_id>/change-password", methods=['PUT'])
def change_password(customer_id):
    data = request.json
    current_password = data.get('current_password')
    new_password = data.get('new_password')
    sql = 'Select * from customer where id = \'{}\''.format(customer_id)
    result1 = get_data_customer(sql)
    if current_password == result1[6]:
        sql1 = 'update customer set password = \'{}\' where id = {}'.format(new_password, customer_id)
        update_customer(sql1)
        result = get_data_customer(sql)
        if new_password == result[6]:
            return jsonify({
                "code": 200,
                "user_message": "Đổi mật khẩu thành công",
                "internal_message": "Request thành công"
            })
        else:
            return  jsonify({
                "internal_message": "Có lỗi khi cập nhật CSDL"
            })
    else:
        return jsonify({
            "code": 200,
            "user_message": "Mật khẩu không chính xác",
            "internal_message": "Request thành công"
        })

#Api quên mật khẩu
@customer.route("/v1/customers/email/forgot-password", methods=['POST'])
def forgot_password():
    data = request.json
    email_sent = data.get('email')
    code = random.randint(000000, 999999)
    email = 'minhviphb98@gmail.com'
    password = 'medfgqumdpehiipn'
    sql1 = "Select id from customer where email = \'{}\'".format(email_sent)
    created_at = datetime.now()
    temp = get_data_customer(sql1)
    if temp != None:
        customer_id = int(temp[0])
        sql = "Insert into manager_code (customer_id, code, action, created_at) values ({}, {}, \'{}\', \'{}\')".format(customer_id, code, 'forgot-password', created_at)
        update_manager_code(sql)
        try:
            session = smtplib.SMTP('smtp.gmail.com', 587)
            session.starttls()
            session.login(email, password)
            mail_content = str(code)
            session.sendmail(email, email_sent, mail_content)
            return jsonify({
                "code": 200,
                "user_message": "Mã OTP đã được gửi vào email, bạn hãy vào email để check",
                "internal_message": "Request thành công"
            })
        #Bắt lỗi không thể kết nối với máy chủ. Cài đặt kết nối không hợp lệ?
        except (gaierror, ConnectionRefusedError):
            print('Failed to connect to the server. Bad connection settings?')
        #Không thể kết nối với máy chủ. Người dùng sai mật khẩu hoặc tài khoản?
        except smtplib.SMTPServerDisconnected:
            print('Failed to connect to the server. Wrong user/password?')
        #Bắt các ngoại lệ khác
        except smtplib.SMTPException as e:
            print('SMTP error occurred: ' + str(e))
    else:
        return jsonify({
            "code": 200,
            "user_message": "email không đúng hoặc chưa được đăng ký",
            "internal_message": "Request thành công"
        })

#Api thay mới mật khẩu
@customer.route("/v1/customers/<int:customer_id>/new-password", methods=['PUT'])
def change_password_new(customer_id):
    data = request.json
    new_password = data.get('new_password')
    verification = data.get('verification')
    sql = "Select created_at from manager_code where customer_id = {} and action = 'forgot-password'".format(customer_id)
    created_at = get_data_manager_code(sql)
    now_time = datetime.now()
    temp = now_time - created_at[0]
    if temp.seconds > 300:
        sql1 = 'Delete from manager_code where customer_id = {}'.format(customer_id)
        update_manager_code(sql1)
        return jsonify({
            "code": 200,
            "user_message": "Mã xác nhận không đúng",
            "internal_message": "Request thành công"
        })
    else:
        sql2 = 'Select code from manager_code where customer_id = {}'.format(customer_id)
        result = get_data_manager_code(sql2)
        if result[0] == verification:
            sql3 = 'Update customer set password = {} where id = {}'.format(new_password, customer_id)
            update_customer(sql3)
            sql4 = 'Delete from manager_code where customer_id = {}'.format(customer_id)
            update_manager_code(sql4)
            return jsonify({
                "code": 200,
                "user_message": "Đổi mật khẩu thành công",
                "internal_message": "Request thành công"
            })