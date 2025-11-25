import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Noahvand1",
    database="SFPL_DB"
)

cur = conn.cursor()
cur.execute("SELECT * FROM sfpl_db_lib;")

for row in cur.fetchall():
    print(row)

cur.close()
conn.close()
