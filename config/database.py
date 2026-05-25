import pymysql

class Database:

    @staticmethod
    def get_connection():

        return pymysql.connect(
            host="instancia-iot.czc0w6oauwge.us-east-1.rds.amazonaws.com",
            user="admin",
            password="Admin12345#",
            database="carrito_iot",
            cursorclass=pymysql.cursors.DictCursor
        )