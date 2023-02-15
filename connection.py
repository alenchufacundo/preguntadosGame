import pymysql

class DataBase:
    def __init__(self):
        self.connect = pymysql.connect(
            host = "db4free.net",
            port = 3306,
            user = "rootafr",
            password = '6338.hola',
            db = "preguntados"
            )
        self.cursor = self.connect.cursor()