#Task 3 Load Data from SQL Database
import pandas as pd 
import sqlite3

conn = sqlite3.connect('./sample.db')

#Create Table Employees
query = """
CREATE TABLE IF NOT EXISTS Employees(
    id Integer PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary Integer
)

"""
conn.execute(query)


#Inserting 5 records
Employee = {
    (1,'Shreyas','AIDS',60000),
    (2,'Amit','CS',40000),
    (3,'Smit','Cloud',70000),
    (4,'Omit','Dev',20000),
    (5,'Lmit','Design',10000)
}

conn.executemany(
    'INSERT OR IGNORE INTO Employees ("id","name","department","salary") Values(?,?,?,?)',
    Employee
)
conn.commit()

#Read the data

df = pd.read_sql_query('SELECT * from Employees',conn)
print(df)
