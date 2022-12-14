from src.models.models import conn_SQL



def update_gallery(id , type,url):
    conn = conn_SQL()
    mydb = conn.connection_db()
    cursor = mydb.cursor()
    sql = "UPDATE gallery SET type = \'{}\',url = \'{}\' WHERE id = {} ".format( type,url, id)
    cursor.execute(sql)
    mydb.commit()

def insert_gallery(product_id,type,url):
    conn = conn_SQL()
    mydb = conn.connection_db()
    cursor = mydb.cursor()
    sql = "insert into gallery(product_id,type,url) values(\'{}\',\'{}\',\'{}\')".format( product_id,type,url)
    cursor.execute(sql)
    mydb.commit()

#Lấy 1 bản ghi
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

