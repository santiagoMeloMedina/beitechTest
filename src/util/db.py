
import mysql.connector as connector
import constant.connection as CONN

class DBClient:
    def __init__(self):
        self.conn = connector.connect(
            host=CONN.DB_HOST,
            port=CONN.DB_PORT,
            user=CONN.DB_USER,
            database=CONN.DB_NAME,
            password=CONN.DB_PASSWORD,
            ssl_disabled=CONN.DB_SSL_DISABLE
        )
        self.cursor = self.conn.cursor(dictionary=True)
    
    def query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def crud(self, query):
        response = self.cursor.execute(query)
        self.conn.commit()
        return { "rows": self.cursor.rowcount, "lastid": self.cursor.lastrowid }


