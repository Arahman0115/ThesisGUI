import mysql
import mysql.connector

class DatabaseConnection:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor(dictionary=True)

db_connection = DatabaseConnection(host='localhost', user='root', password="", database='pharmgui')