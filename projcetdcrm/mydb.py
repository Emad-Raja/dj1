import mysql.connector

dataBase=mysql.connector.connect(
 host='localhost',
 user='root',
 password='Raja@1122'
)

cursorObject=dataBase.cursor()

cursorObject.execute("CREATE DATABASE emad")

print("CREATED")