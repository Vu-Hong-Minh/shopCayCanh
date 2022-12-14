from src.models.models import conn_SQL

def update_product_id(product_id,id):
    conn = conn_SQL()
    mydb = conn.connection_db()
    cursor = mydb.cursor()
    sql = "update product_category set product_id = {} where id = {}".format(product_id,id)
    cursor.execute(sql)
    mydb.commit()
def update_category_id(category_id,id):
    conn = conn_SQL()
    mydb = conn.connection_db()
    cursor = mydb.cursor()
    sql = "update product_category set category_id = {} where id = {}".format(category_id,id)
    cursor.execute(sql)
    mydb.commit()

def insert_product_category(product_id,category_id):
    conn = conn_SQL()
    mydb = conn.connection_db()
    cursor = mydb.cursor()
    sql = "insert into product_category (product_id,category_id) values ({},{})".format(product_id,category_id)
    cursor.execute(sql)
    mydb.commit()