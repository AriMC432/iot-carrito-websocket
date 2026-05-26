import pymysql

class Database:

    @staticmethod
    def get_connection():

        return pymysql.connect(
            host="localhost",
            user="root",
            password="0423",
            database="carrito_iot",
            cursorclass=pymysql.cursors.DictCursor
        )