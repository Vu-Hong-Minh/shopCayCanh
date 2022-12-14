from src.models.models import conn_SQL

# Lấy 1 bản ghi
def get_data_manager_code(sql):
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
def update_manager_code(sql):
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