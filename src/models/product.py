from src.models.models import conn_SQL

def get_data_products(sql):
    #Hàm lấy danh sách sản phẩm
    try:
        conn = conn_SQL()
        mydb = conn.connection_db()
        cursor = mydb.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()
        return row

    finally:
        # Đóng kết nối (Close connection).
        cursor.close()
        mydb.close()

def get_data_product(sql):
    # Hàm lấy thông tin sản phẩm
    try:
        conn = conn_SQL()
        mydb = conn.connection_db()
        cursor = mydb.cursor()
        cursor.execute(sql)
        row = cursor.fetchone()
        return row

    finally:
        # Đóng kết nối (Close connection).
        cursor.close()
        mydb.close()