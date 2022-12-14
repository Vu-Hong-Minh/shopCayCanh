from src.models.models import conn_SQL


def get_detail_order(id):
    conn = conn_SQL()
    mydb = conn.connection_db()
    cursor = mydb.cursor()
    sql = "select product.name ,detail_order.id , detail_order.quantity, detail_order.price, detail_order.money from detail_order inner join product on product.id = detail_order.product_id where order_id  = \'{}\' ".format(id)
    cursor.execute(sql)
    row = cursor.fetchall()
    return row


def update_detail_order(id, quantity, price, money):
    conn = conn_SQL()
    mydb = conn.connection_db()
    cursor = mydb.cursor()
    sql = "update detail_order set quantity = \'{}\',price = \'{}\',money = \'{}\' where id = \'{}\'".format(quantity,price,money,id)
    cursor.execute(sql)
    mydb.commit()


def get_total_money(id):
    conn = conn_SQL()
    mydb = conn.connection_db()
    cursor = mydb.cursor()
    sql = "SELECT SUM(money) FROM detail_order where order_id  = \'{}\' ".format(id)
    cursor.execute(sql)
    row = cursor.fetchone()
    return row

    
def insert_detail_order(receipt_id,product_id,quantity,price,money):
    conn = conn_SQL()
    mydb = conn.connection_db()
    cursor = mydb.cursor()
    sql = "INSERT INTO detail_order(receipt_id,product_id,quantity,price,money) VALUES(\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')".format(receipt_id,product_id,quantity,price,money)
    cursor.execute(sql)
    mydb.commit()
