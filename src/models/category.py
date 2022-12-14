from src.models.models import conn_SQL

per_page = 10

def get_category(page):
    conn = conn_SQL()
    mydb = conn.connection_db()
    cursor = mydb.cursor()
    start = (int(page) - 1)*per_page
    sql = "select * from category limit {},{}".format(start, per_page)
    cursor.execute(sql)
    row = cursor.fetchall()
    return row


def insert_category(name, status):
    conn = conn_SQL()
    mydb = conn.connection_db()
    cursor = mydb.cursor()
    sql = "INSERT INTO category(name,status) VALUES(\'{}\',\'{}\')".format(name, status)
    cursor.execute(sql)
    mydb.commit()
    sql1 = " SELECT @@IDENTITY asLastID"
    cursor.execute(sql1)
    row = cursor.fetchone()
    return row 



def update_category(id, name, status):
    conn = conn_SQL()
    mydb = conn.connection_db()
    cursor = mydb.cursor()
    sql = "UPDATE category SET name = \'{}\',status = \'{}\' WHERE id = {} ".format(name, status, id)
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

def get_category_by_name(name):
    conn = conn_SQL()
    mydb = conn.connection_db()
    cursor = mydb.cursor()
    sql = "select * from category where name = \'{}\'".format(name)
    cursor.execute(sql)
    row = cursor.fetchone()
    return row


