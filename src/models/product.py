from src.models.models import conn_SQL
per_page = 10

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

def get_products(page):
    conn = conn_SQL()
    mydb = conn.connection_db()
    cursor = mydb.cursor()
    start = (int(page) - 1)*per_page
    sql = "select * from product limit {},{}".format(start, per_page)
    cursor.execute(sql)
    row = cursor.fetchall()
    return row


def insert_product(name,uses,science_name,price,size,image,description,care_plant,status,created_at,created_by):
    conn = conn_SQL()
    mydb = conn.connection_db()
    cursor = mydb.cursor()
    sql = "INSERT INTO product(name,uses,science_name,price,size,image,description,care_plant,status,created_at,created_by) VALUES(\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')".format(name,uses,science_name,price,size,image,description,care_plant,status,created_at,created_by)
    cursor.execute(sql)
    mydb.commit()
    sql1 = " SELECT @@IDENTITY asLastID"
    cursor.execute(sql1)
    row = cursor.fetchone()
    return row
def get_created_by(created_by):
    conn = conn_SQL()
    mydb = conn.connection_db()
    cursor = mydb.cursor()
    sql = "SELECT employee.full_name FROM product inner join employee on product.created_by = employee.id where created_by = {}".format(created_by)
    cursor.execute(sql)
    row = cursor.fetchone()
    return row
def get_updated_by(updated_by):
    conn = conn_SQL()
    mydb = conn.connection_db()
    cursor = mydb.cursor()
    sql = "SELECT employee.full_name FROM product inner join employee on product.updated_by = employee.id where updated_by = {}".format(updated_by)
    cursor.execute(sql)
    row = cursor.fetchone()
    return row


def update_product(id, name, science_name, price, size, image, uses, description, care_plant, status,updated_by,updated_at):
    conn = conn_SQL()
    mydb = conn.connection_db()
    cursor = mydb.cursor()
    sql = "UPDATE category SET name = \'{}\'science_name = \'{}\',price = \'{}\',size = \'{}\',image = \'{}\',uses = \'{}\',description = \'{}\',care_plant = \'{}\',status = \'{}\',updated_by = \'{}\',updated_at = \'{}\' WHERE id = {} ".format(name, science_name, price, size, image, uses, description, care_plant, status,updated_by,updated_at, id)
    cursor.execute(sql)
    mydb.commit()

def get_category_by_id(id):
    conn = conn_SQL()
    mydb = conn.connection_db()
    cursor = mydb.cursor()
    sql = "select * from category where id = {}".format(id)
    cursor.execute(sql)
    row = cursor.fetchone()
    return row

def get_product_by_name(name):
    conn = conn_SQL()
    mydb = conn.connection_db()
    cursor = mydb.cursor()
    sql = "select * from product where name = \'{}\'".format(name)
    cursor.execute(sql)
    row = cursor.fetchone()
    return row

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