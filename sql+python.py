import mysql.connector
shubh = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(shubh.is_connected())
cur = shubh.cursor()
cur.execute('show databases')
for i in cur:
    print(i)