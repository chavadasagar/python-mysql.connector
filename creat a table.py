import mysql.connector

con = mysql.connector.connect(host="localhost",user="root",password="",database='dbs') #connection

cur = con.cursor()

cur.execute("create table sagar (no varchar(3) not null,name varchar(200) not null)")

print("table create successfuly!!!");



