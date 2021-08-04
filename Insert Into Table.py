import mysql.connector

con = mysql.connector.connect(host="localhost",user="root",password="",database='dbs') #connection

cur = con.cursor()

#Insert Into Table

sql = "insert into sagar values(%s,%s)"
val = ("1","ram")

cur.execute(sql,val)

con.commit()


print(cur.rowcount, "record inserted.")
