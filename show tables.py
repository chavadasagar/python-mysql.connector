import mysql.connector

con = mysql.connector.connect(host="localhost",user="root",password="",database='dbs') #connection

cur = con.cursor()

#Check if Table Exists

cur.execute("show tables")


for x in cur:
    print(x)


