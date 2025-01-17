import mysql.connector as c
mydb=c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="vaishc1"
)

mycursor = mydb.cursor()
country=input("Enter country name:")
sql_query="delete from economy where country= %s;"
mycursor.execute(sql_query,(country,))
mydb.commit()