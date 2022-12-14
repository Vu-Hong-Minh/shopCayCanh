from src.models.models import conn_SQL

per_page = 10

def get_receiver(page):
    conn = conn_SQL()
    mydb = conn.connection_db()
    cursor = mydb.cursor()
    start = (int(page) - 1)*per_page
    sql = "select * from receiver limit {},{}".format(start, per_page)
    cursor.execute(sql)
    row = cursor.fetchall()
    return row

def update_receiver(id, full_name,phone,address):
    conn = conn_SQL()
    mydb = conn.connection_db()
    cursor = mydb.cursor()
    sql = "UPDATE receiver SET full_name = \'{}\',phone = \'{}\',address = \'{}\'WHERE id = {} ".format(full_name,phone,address, id)
    cursor.execute(sql)
    mydb.commit()

def get_receiver_by_id(id):
    conn = conn_SQL()
    mydb = conn.connection_db()
    cursor = mydb.cursor()
    sql = "select * from receiver where id = {}".format(id)
    cursor.execute(sql)
    row = cursor.fetchone()
    return row