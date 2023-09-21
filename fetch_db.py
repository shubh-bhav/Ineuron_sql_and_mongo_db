import mysql.connector
shubh = mysql.connector.connect(
    host = "localhost",
    user = "abc",
    password = "password"
)

cur = shubh.cursor()
cur.execute('select * from fsds_db.fsds1')
for i in cur:
    print(i)