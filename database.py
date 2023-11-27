import sqlite3

conn = sqlite3.connect('acer.db')
print("opened database successfully")

conn.execute('''create table employee1(ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
AGE INT NOT NULL,
ADDRESS CHAR(50),
SALARY REAL);''')

print("table created successfully")
conn.close()