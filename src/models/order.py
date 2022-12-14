from src.models.models import conn_SQL


def get_order_by_id(id):
    conn = conn_SQL()
    mydb = conn.connection_db()
    cursor = mydb.cursor()
    sql = "select * from orders where id = {}".format(id)
    cursor.execute(sql)
    row = cursor.fetchone()
    return row


def update_order(id, updated_by, updated_at, total_money,status):
    conn = conn_SQL()
    mydb = conn.connection_db()
    cursor = mydb.cursor()
    sql = "UPDATE orders SET updated_by = \'{}\',updated_at = \'{}\',total_money = \'{}\',status = \'{}\' WHERE id = {} ".format(
        updated_by, updated_at, total_money,status, id)
    cursor.execute(sql)
    mydb.commit()
