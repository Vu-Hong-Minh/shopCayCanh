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
