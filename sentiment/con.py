import mysql.connector
from mysql.connector import errorcode
from django.conf import settings

class MYSQLConnection:
    def __init__(self):
        self.DB_HOST=settings.DB_HOST
        self.DB_NAME=settings.DB_NAME
        self.DB_USER=settings.DB_USER
        self.DB_PASS=settings.DB_PASS
        self.DB_PORT=settings.DB_PORT

    def conn(self):
        try:
            cnx = mysql.connector.connect(
                user=self.DB_USER, 
                password=self.DB_PASS,
                host=self.DB_HOST,
                database=self.DB_NAME)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
            return False
        else:
            return cnx

    def insert(self, cnx, name, email, password, admin):
        add_user = ("INSERT INTO user "
               "(user_name, user_email, user_pass, admin) "
               "VALUES (%s, %s, %s, %s)")
        data_user =  (name, email, password, admin)
        cursor = cnx.cursor()
        cursor.execute(add_user, data_user)
        user_no = cursor.lastrowid
        cnx.commit()
        cursor.close()
        return user_no