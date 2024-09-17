#GUI for Adding an Instructor to the Database

import sqlite3
from tkinter import *

###Functions
# function for clearing the contents of all entry boxes 
def clear_all():
	tid_field.delete(0, END)
	firstName_field.delete(0, END)
	middleInital_field.delete(0, END)
	lastName_field.delete(0, END)
	degreeSuffix_field.delete(0, END)
	email_field.delete(0, END)
	department_field.delete(0, END)
	officePhone_field.delete(0, END)
	officeLocation_field.delete(0, END)

# function to display text when button is clicked
def clicked():
	lbl10.configure(text = "Instructor Added!")
	SQLinsert()

# SQL Insert function
def SQLinsert():
	tid_data = tid_field.get()
	firstName_data = firstName_field.get()
	middleInitial_data = middleInital_field.get()
	lastName_data = lastName_field.get()
	degreeSuffix_data = degreeSuffix_field.get()
	email_data = email_field.get()
	department_data = department_field.get()
	officePhone_data = officePhone_field.get()
	officeLocation_data = officeLocation_field.get()
	sql = '''INSERT INTO instructor (tid, firstName, middleInitial, lastName, degreeSuffix, email, department, officePhone, officeLocation) 
			VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'''
	c.execute(sql, (tid_data, firstName_data, middleInitial_data, lastName_data, degreeSuffix_data, email_data, department_data, officePhone_data, officeLocation_data))
	conn.commit()


###SQL
# connect to our database
conn = sqlite3.connect("C:\CS 2700 51\CS 2700 DB\sis_db_2700_2")

# define cursor
c = conn.cursor()


###GUI 
# GUI Creation
root = Tk()
root.title("Add Instructor")
root.geometry('350x450')

# Labels
lbl1 = Label(root, text = "Enter Instructor ID")
lbl2 = Label(root, text = "Enter First Name")
lbl3 = Label(root, text = "Enter Middle Initial")
lbl4 = Label(root, text = "Enter Last Name")
lbl5 = Label(root, text = "Enter Degree Suffix")
lbl6 = Label(root, text = "Enter Email")
lbl7 = Label(root, text = "Enter Department")
lbl8 = Label(root, text = "Enter Office Phone ")
lbl9 = Label(root, text = "Enter Office Location")
lbl10 = Label(root, text = "Pending")

lbl1.grid(row = 1, column = 0, padx = 10, pady = 10) 
lbl2.grid(row = 2, column = 0, padx = 10, pady = 10)
lbl3.grid(row = 3, column = 0, padx = 10, pady = 10)
lbl4.grid(row = 4, column = 0, padx = 10, pady = 10)
lbl5.grid(row = 5, column = 0, padx = 10, pady = 10)
lbl6.grid(row = 6, column = 0, padx = 10, pady = 10)
lbl7.grid(row = 7, column = 0, padx = 10, pady = 10)
lbl8.grid(row = 8, column = 0, padx = 10, pady = 10)
lbl9.grid(row = 9, column = 0, padx = 10, pady = 10)
lbl10.grid(row = 10, column = 0, padx = 10, pady = 10)

# Fields
tid_field = Entry(root)
firstName_field = Entry(root)
middleInital_field = Entry(root)
lastName_field = Entry(root)
degreeSuffix_field = Entry(root)
email_field = Entry(root)
department_field = Entry(root)
officePhone_field = Entry(root)
officeLocation_field = Entry(root)

tid_field.grid(row = 1, column = 1, padx = 10, pady = 10) 
firstName_field.grid(row = 2, column = 1, padx = 10, pady = 10)
middleInital_field.grid(row = 3, column = 1, padx = 10, pady = 10)
lastName_field.grid(row = 4, column = 1, padx = 10, pady = 10)
degreeSuffix_field.grid(row = 5, column = 1, padx = 10, pady = 10)
email_field.grid(row = 6, column = 1, padx = 10, pady = 10)
department_field.grid(row = 7, column = 1, padx = 10, pady = 10)
officePhone_field.grid(row = 8, column = 1, padx = 10, pady = 10)
officeLocation_field.grid(row = 9, column = 1, padx = 10, pady = 10)

# Buttons
#Register
btn_reg = Button(root, text = "Add Instructor", fg = "red", command=clicked)
btn_reg.grid(row = 10, column = 1)

#Clear 
btn_clr = Button(root, text = "Clear Entries", fg = "black", command = clear_all)
btn_clr.grid(row = 11, column = 1, pady = 10)


root.mainloop()
