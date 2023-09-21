# creating table in a newly created db
import mysql.connector
shubh = mysql.connector.connect(
    host = "localhost",
    user = "abc",
    password = "password"
)

cur = shubh.cursor()
cur.execute("use fsds_db")

cur.execute('create table fsds1 (name varchar(40) , roll_no int , mail_id varchar(50))')

cur.execute("insert into fsds1 value ('shubham',2020,'shubhmech11@gmail.com')")

shubh.commit()

 