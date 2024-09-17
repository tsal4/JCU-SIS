#GUI for Adding a Course to the Database

import sqlite3
from tkinter import *

###Functions
# function for clearing the contents of all entry boxes 
def clear_all():
	cid_field.delete(0, END)
	courseTitle_field.delete(0, END)
	department_field.delete(0, END)
	courseNumber_field.delete(0, END)
	courseSection_field.delete(0, END)
	creditHours_field.delete(0, END)
	seats_field.delete(0, END)
	core_field.delete(0, END)

# function to display text when button is clicked
def clicked():
	lbl9.configure(text = "Course Added!")
	SQLinsert()

# SQL Insert function
def SQLinsert():
	cid_data = cid_field.get()
	courseTitle_data = courseTitle_field.get()
	department_data = department_field.get()
	courseNumber_data = courseNumber_field.get()
	courseSection_data = courseSection_field.get()
	creditHours_data = creditHours_field.get()
	seats_data = seats_field.get()
	core_data = core_field.get()
	sql = '''INSERT INTO course (cid, courseTitle, department, courseNumber, courseSection, creditHours, seats, core) 
				VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
	c.execute(sql, (cid_data, courseTitle_data, department_data, courseNumber_data, courseSection_data, creditHours_data, seats_data, core_data))
	conn.commit()


###SQL
# connect to our database
conn = sqlite3.connect("C:\CS 2700 51\CS 2700 DB\sis_db_2700_2")

# define cursor
c = conn.cursor()


###GUI 
# GUI Creation
root = Tk()
root.title("Add Course")
root.geometry('350x450')

# Labels
lbl1 = Label(root, text = "Enter Course ID")
lbl2 = Label(root, text = "Enter Course Title")
lbl3 = Label(root, text = "Enter Department")
lbl4 = Label(root, text = "Enter Course Number")
lbl5 = Label(root, text = "Enter Course Section")
lbl6 = Label(root, text = "Enter Credit Hours")
lbl7 = Label(root, text = "Enter the Number of Seats")
lbl8 = Label(root, text = "Core Requirement? (Y/N)")
lbl9 = Label(root, text = "Pending")

lbl1.grid(row = 1, column = 0, padx = 10, pady = 10) 
lbl2.grid(row = 2, column = 0, padx = 10, pady = 10)
lbl3.grid(row = 3, column = 0, padx = 10, pady = 10)
lbl4.grid(row = 4, column = 0, padx = 10, pady = 10)
lbl5.grid(row = 5, column = 0, padx = 10, pady = 10)
lbl6.grid(row = 6, column = 0, padx = 10, pady = 10)
lbl7.grid(row = 7, column = 0, padx = 10, pady = 10)
lbl8.grid(row = 8, column = 0, padx = 10, pady = 10)
lbl9.grid(row = 9, column = 0, padx = 10, pady = 10)

# Fields
cid_field = Entry(root)
courseTitle_field = Entry(root)
department_field = Entry(root)
courseNumber_field = Entry(root)
courseSection_field = Entry(root)
creditHours_field = Entry(root)
seats_field = Entry(root)
core_field = Entry(root)

cid_field.grid(row = 1, column = 1, padx = 10, pady = 10) 
courseTitle_field.grid(row = 2, column = 1, padx = 10, pady = 10)
department_field.grid(row = 3, column = 1, padx = 10, pady = 10)
courseNumber_field.grid(row = 4, column = 1, padx = 10, pady = 10)
courseSection_field.grid(row = 5, column = 1, padx = 10, pady = 10)
creditHours_field.grid(row = 6, column = 1, padx = 10, pady = 10)
seats_field.grid(row = 7, column = 1, padx = 10, pady = 10)
core_field.grid(row = 8, column = 1, padx = 10, pady = 10)

# Buttons
#Register
btn_reg = Button(root, text = "Add Course", fg = "red", command=clicked)
btn_reg.grid(row = 9, column = 1)

#Clear 
btn_clr = Button(root, text = "Clear Entries", fg = "black", command = clear_all)
btn_clr.grid(row = 10, column = 1, pady = 10)


root.mainloop()
