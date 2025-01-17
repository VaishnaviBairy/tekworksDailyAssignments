import mysql.connector as c

# Establish connection to the database
mydb = c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="vaishc1"
)

mycursor = mydb.cursor()

country = input("Enter the country name whose details you want to update: ")

gdp = float(input("Enter new GDP: "))
inflation_rate = float(input("Enter new inflation rate: "))
unemployment_rate = float(input("Enter new unemployment rate: "))
currency = input("Enter new currency: ")
region = input("Enter new region: ")

update_query = """
UPDATE economy
SET gdp = %s, inflation_rate = %s, unemployment_rate = %s, currency = %s, region = %s
WHERE country = %s;
"""

mycursor.execute(update_query, (gdp, inflation_rate, unemployment_rate, currency, region, country))

mydb.commit()

if mycursor.rowcount > 0:
    print(f"Details for {country} updated successfully.")
else:
    print(f"No record found for {country} to update.")

mycursor.close()
mydb.close()
