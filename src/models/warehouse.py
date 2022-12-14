from src.models.models import conn_SQL

def update_product_id(product_id,id):
    conn = conn_SQL()
    mydb = conn.connection_db()
    cursor = mydb.cursor()
    sql = "update product_category set product_id = {} where id = {}".format(product_id,id)
    cursor.execute(sql)
    mydb.commit()
def update_warehouse(product_id,quantity):
    conn = conn_SQL()
    mydb = conn.connection_db()
    cursor = mydb.cursor()
    sql = "update warehouse set quantity = quantity + \'{}\' where product_id = {}".format(quantity,product_id)
    cursor.execute(sql)
    mydb.commit()

def insert_warehouse(product_id,quantity):
    conn = conn_SQL()
    mydb = conn.connection_db()
    cursor = mydb.cursor()
    sql = "insert into warehouse(product_id,quantity) values ({},{})".format(product_id,quantity)
    cursor.execute(sql)
    mydb.commit()