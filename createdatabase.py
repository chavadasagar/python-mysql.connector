import mysql.connector

con = mysql.connector.connect(host="localhost",user="root",password="") #connection

cur = con.cursor()

cur.execute("create database sagar") #query

