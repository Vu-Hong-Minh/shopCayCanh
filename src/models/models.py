import mysql.connector
# Kết nối vào database.
class conn_SQL:
    def __init__(self, host='127.0.0.1', db='caycanh1', user='root', password='123123'):
        self.host = host
        self.db = db
        self.user = user
        self.password = password

    def connection_db(self):
        mydb = mysql.connector.connect(host=self.host, database=self.db, user=self.user, password=self.password)
        return mydb
