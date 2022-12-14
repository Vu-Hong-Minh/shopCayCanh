from src.models.models import conn_SQL

per_page = 10

def get_customer(page):
    conn = conn_SQL()
    mydb = conn.connection_db()
    cursor = mydb.cursor()
    start = (int(page) - 1)*per_page
    sql = "select * from customer limit {},{}".format(start, per_page)
    cursor.execute(sql)
    row = cursor.fetchall()
    return row

def update_customer(id, full_name, gender,email,phone,address,updated_at,updated_by):
    conn = conn_SQL()
    mydb = conn.connection_db()
    cursor = mydb.cursor()
    sql = "UPDATE customer SET full_name = \'{}\',gender = \'{}\',email = \'{}\',phone = \'{}\',address = \'{}\',updated_at = \'{}\',updated_by = \'{}\'WHERE id = {} ".format( full_name, gender,email,phone,address,updated_at,updated_by, id)
    cursor.execute(sql)
    mydb.commit()

def get_customer_by_id(id):
    conn = conn_SQL()
    mydb = conn.connection_db()
    cursor = mydb.cursor()
    sql = "select * from category where id = {}".format(id)
    cursor.execute(sql)
    row = cursor.fetchone()
    return row

# Lấy 1 bản ghi
def get_data_customer(sql):
    try:
        conn = conn_SQL()
        mydb = conn.connection_db()
        cursor = mydb.cursor()
        cursor.execute(sql)
        result = cursor.fetchone()
        return result

    finally:
        # Đóng kết nối (Close connection).
        cursor.close()
        mydb.close()

# Cập nhật bản ghi
def update_customer(sql):
    try:
        conn = conn_SQL()
        mydb = conn.connection_db()
        cursor = mydb.cursor()
        cursor.execute(sql)
        mydb.commit()
    finally:
        # Đóng kết nối (Close connection).
        cursor.close()
        mydb.close()