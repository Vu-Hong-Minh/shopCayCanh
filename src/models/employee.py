from src.models.models import conn_SQL

per_page = 10

def get_employee(page):
    conn = conn_SQL()
    mydb = conn.connection_db()
    cursor = mydb.cursor()
    start = (int(page) - 1)*per_page
    sql = "select * from employee limit {},{}".format(start, per_page)
    cursor.execute(sql)
    row = cursor.fetchall()
    return row


def insert_employee(role_id,full_name, phone,date_of_birth,gender,address,job_postion,password,status,created_at):
    conn = conn_SQL()
    mydb = conn.connection_db()
    cursor = mydb.cursor()
    sql = "INSERT INTO employee( role_id,full_name, phone,date_of_birth,gender,address,job_postion,password,status,created_at) VALUES(\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')".format(role_id,full_name, phone,date_of_birth,gender,address,job_postion,password,status,created_at)
    cursor.execute(sql)
    mydb.commit()




def update_employee(id, full_name, phone,date_of_birth,gender,address,job_postion,password,updated_at,status):
    conn = conn_SQL()
    mydb = conn.connection_db()
    cursor = mydb.cursor()
    sql = "UPDATE employee SET full_name = \'{}\',phone = \'{}\',date_of_birth = \'{}\',gender = \'{}\',address = \'{}\',job_postion = \'{}\',password = \'{}\',updated_at = \'{}\',status = \'{}\' WHERE id = {} ".format(full_name, phone,date_of_birth,gender,address,job_postion,password,updated_at,status, id)
    cursor.execute(sql)
    mydb.commit()

def get_employee_by_id(id):
    conn = conn_SQL()
    mydb = conn.connection_db()
    cursor = mydb.cursor()
    sql = "select * from employee where id = {}".format(id)
    cursor.execute(sql)
    row = cursor.fetchone()
    return row

def get_employee_by_phone(phone):
    conn = conn_SQL()
    mydb = conn.connection_db()
    cursor = mydb.cursor()
    sql = "select * from employee where phone = \'{}\'".format(phone)
    cursor.execute(sql)
    row = cursor.fetchone()
    return row


