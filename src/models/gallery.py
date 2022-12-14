from src.models.models import conn_SQL

def get_data_galleries(sql):
    # Hàm lấy danh sách ảnh chi tiết sản phẩm
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