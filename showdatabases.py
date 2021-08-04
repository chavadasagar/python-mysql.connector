import mysql.connector

con = mysql.connector.connect(host="localhost",user="root",password="") #connection

cur = con.cursor()

cur.execute("show databases")

for x in cur:
    print(x)


