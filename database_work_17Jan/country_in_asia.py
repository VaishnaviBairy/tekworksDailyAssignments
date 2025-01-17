import mysql.connector as c

# Establish connection to the database
mydb = c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="vaishc1"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM economy WHERE region = 'Asia'")

result = mycursor.fetchall()

if result:
    print("Displaying records for countries in Asia:")
    for row in result:
        print(row)
else:
    print("No records found for countries in Asia.")

# Close the cursor and database connection
mycursor.close()
mydb.close()
