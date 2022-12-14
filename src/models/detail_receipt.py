from src.models.models import conn_SQL


def get_detail_receipt(id):
    conn = conn_SQL()
    mydb = conn.connection_db()
    cursor = mydb.cursor()
    sql = "select product.name ,detail_receipt.id , detail_receipt.quantity, detail_receipt.price, detail_receipt.money from detail_receipt inner join product on product.id = detail_receipt.product_id where receipt_id  = \'{}\' ".format(id)
    cursor.execute(sql)
    row = cursor.fetchall()
    return row


def update_detail_receipt(id, quantity, price, money):
    conn = conn_SQL()
    mydb = conn.connection_db()
    cursor = mydb.cursor()
    sql = "update detail_receipt set quantity = \'{}\',price = \'{}\',money = \'{}\' where id = \'{}\'".format(quantity,price,money,id)
    cursor.execute(sql)
    mydb.commit()
def get_total_money(id):
    conn = conn_SQL()
    mydb = conn.connection_db()
    cursor = mydb.cursor()
    sql = "SELECT SUM(money) FROM detail_receipt where receipt_id  = \'{}\' ".format(id)
    cursor.execute(sql)
    row = cursor.fetchone()
    return row
def insert_detail_receipt(receipt_id,product_id,quantity,price,money):
    conn = conn_SQL()
    mydb = conn.connection_db()
    cursor = mydb.cursor()
    sql = "INSERT INTO detail_receipt(receipt_id,product_id,quantity,price,money) VALUES(\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')".format(receipt_id,product_id,quantity,price,money)
    cursor.execute(sql)
    mydb.commit()
