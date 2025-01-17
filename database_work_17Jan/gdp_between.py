import mysql.connector as c

# Establish connection to the database
mydb = c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="vaishc1"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM economy WHERE gdp BETWEEN 10 AND 30")

result = mycursor.fetchall()

if result:
    print("Displaying countries with GDP between 10 and 30 trillion:")
    for row in result:
        print(row)
else:
    print("No countries found with GDP between 10 and 30 trillion.")

# Close the cursor and database connection
mycursor.close()
mydb.close()
