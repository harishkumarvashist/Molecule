import mysql.connector

BM_db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="bifunctiona_modalities",
)
my_cursor=BM_db.cursor()

my_cursor.execute("SHOW DATABASES")

for DB in my_cursor:
    print(DB)