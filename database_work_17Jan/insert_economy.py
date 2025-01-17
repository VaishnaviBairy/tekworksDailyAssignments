import mysql.connector as c

# Establish connection to the database
mydb = c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="vaishc1"
)
mycursor = mydb.cursor()
print("Enter the following details to add a new record to the economy table:")

country = input("Enter country name: ")
gdp = float(input("Enter GDP (in trillions or billions): "))
inflation_rate = float(input("Enter inflation rate (percentage): "))
unemployment_rate = float(input("Enter unemployment rate (percentage): "))
currency = input("Enter the currency: ")
region = input("Enter the region: ")

insert_data_query = """
INSERT INTO economy (country, gdp, inflation_rate, unemployment_rate, currency, region)
VALUES (%s, %s, %s, %s, %s, %s);
"""
data = (country, gdp, inflation_rate, unemployment_rate, currency, region)

mycursor.execute(insert_data_query, data)

mydb.commit()

print("Record inserted successfully! ")

mycursor.close()
mydb.close()
