import mysql.connector

my_db = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    passwd='root'
)

my_cursor = my_db.cursor()

my_cursor.execute("SHOW DATABASES")

for x in my_cursor:
    print(x)