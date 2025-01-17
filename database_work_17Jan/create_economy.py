import mysql.connector as c
mydb=c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="vaishc1"
)

mycursor = mydb.cursor()
table_query = """CREATE TABLE IF NOT EXISTS economy (country VARCHAR(100),gdp DECIMAL(20,2),
              inflation_rate DECIMAL(5,2),unemployment_rate DECIMAL(5,2),currency VARCHAR(10),region VARCHAR(50));"""
mycursor.execute(table_query)
mydb.commit()
print("Table  created successfully")
mycursor.close()
mydb.close()
