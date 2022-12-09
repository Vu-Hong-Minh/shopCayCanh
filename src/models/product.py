from src.models.models import conn_SQL

def get_product_category(category_id):
    #Hàm lấy danh sách sản phẩm theo id danh mục
    try:
        conn = conn_SQL()
        mydb = conn.connection_db()
        cursor = mydb.cursor()
        sql = "select Table1.name, product.id, product.name from product inner join(select category.name, product_category.product_id from category inner join product_category ON category.id = {} and category.id = product_category.category_id) as Table1 ON Table1.product_id = product.id limit 5".format(category_id)
        cursor.execute(sql)
        row = cursor.fetchall()
        return row

    finally:
        # Đóng kết nối (Close connection).
        cursor.close()
        mydb.close()