import mysql.connector as c

# Establish connection to the database
mydb = c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="vaishc1"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM economy ORDER BY gdp ASC")

result = mycursor.fetchall()

if result:
    print("Displaying countries sorted by GDP in ascending order:")
    for row in result:
        print(row)
else:
    print("No records found.")

mycursor.close()
mydb.close()
