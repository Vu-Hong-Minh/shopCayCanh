from src.models.models import conn_SQL
per_page = 10

def get_receipt_by_id(id):
    conn = conn_SQL()
    mydb = conn.connection_db()
    cursor = mydb.cursor()
    sql = "select * from receipt where id = {}".format(id)
    cursor.execute(sql)
    row = cursor.fetchone()
    return row
def update_receipt(id,updated_by,updated_at,total_money):
    conn = conn_SQL()
    mydb = conn.connection_db()
    cursor = mydb.cursor()
    sql = "UPDATE receipt SET updated_by = \'{}\',updated_at = \'{}\',total_money = \'{}\' WHERE id = {} ".format( updated_by,updated_at,total_money,id)
    cursor.execute(sql)
    mydb.commit()

def insert_receipt(employee_id,created_at,total_money):
    conn = conn_SQL()
    mydb = conn.connection_db()
    cursor = mydb.cursor()
    sql = "insert into receipt(employee_id,created_at,total_money) values(\'{}\',\'{}\',\'{}\') ".format(employee_id,created_at,total_money)
    cursor.execute(sql)
    mydb.commit()
    sql1 = " SELECT @@IDENTITY asLastID"
    cursor.execute(sql1)
    row = cursor.fetchone()
    return row
def get_name_employee(employee_id):
    conn = conn_SQL()
    mydb = conn.connection_db()
    cursor = mydb.cursor()
    sql = "SELECT employee.full_name FROM receipt inner join employee on receipt.employee_id = employee.id where employee_id = {}".format(updated_by)
    cursor.execute(sql)
    row = cursor.fetchone()
    return row


def get_receipt(page):
    conn = conn_SQL()
    mydb = conn.connection_db()
    cursor = mydb.cursor()
    start = (int(page) - 1)*per_page
    sql = "select * from receipt limit {},{}".format(start, per_page)
    cursor.execute(sql)
    row = cursor.fetchall()
    return row