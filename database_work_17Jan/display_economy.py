import mysql.connector as c

# Establish connection to the database
mydb = c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="vaishc1"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM economy")
result = mycursor.fetchall()

print("Displaying all records from the economy table:")
for row in result:
    print(row)

# Close the cursor and database connection
mycursor.close()
mydb.close()
