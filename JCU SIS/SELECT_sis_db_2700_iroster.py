#Prints Instructor Classes

import sqlite3

# connect to our database
conn = sqlite3.connect("C:\CS 2700 51\CS 2700 DB\sis_db_2700_2")

# define cursor
c = conn.cursor()

# SQL select statement
sql = '''SELECT * FROM iroster'''
c.execute(sql)

# get all rows from the SELECT query
rows = c.fetchall()

# display the selected rows
for row in rows:
    print("---------------------------------------------------------------")
    print("Instructor ID: ",row[0])
    print("Instructor Name: ",row[1],row[2])
    print("Course Title: ",row[5]," |  Course ID: ",row[3])
    print("Section #: ",row[4]," | # of Seats: ",row[7])
    print("---------------------------------------------------------------")
    print()
    print()

# close the cursor and the database connection
c.close()
conn.close()
