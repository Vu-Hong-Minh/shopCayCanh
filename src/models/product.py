

from src.models.models import conn_SQL

per_page = 10

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



