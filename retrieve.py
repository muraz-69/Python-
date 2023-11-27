import sqlite3

conn = sqlite3.connect('acer.db')
print("opened database successfully")

cursor = conn.execute("SELECT id,name,age,address,salary from EMPLOYEE")
for row in cursor:
    print("id = ", row[0])
    print("name = ", row[1])
    print("age = ", row[2])
    print("address = ", row[3])
    print("salary = ", row[4])
print("operation done successfully")
conn.close()