#GUI for Course Drop

import sqlite3
from tkinter import *

###Functions
# function for clearing the contents of all entry boxes 
def clear_all():
	sid_field.delete(0, END) 
	cid_field.delete(0, END)

# function to display text when button is clicked
def clicked():
	lbl3.configure(text = "Course Dropped!")
	SQLdelete()

# SQL Insert function
def SQLdelete():
	sid_data = sid_field.get()
	cid_data = cid_field.get()
	sql = '''DELETE FROM StudentCourse WHERE sid = ? AND cid = ?'''
	c.execute(sql, (sid_data, cid_data))
	conn.commit()


###SQL
# connect to our database
conn = sqlite3.connect("C:\CS 2700 51\CS 2700 DB\sis_db_2700_2")

# define cursor
c = conn.cursor()


###GUI
# GUI Creation
root = Tk()
root.title("Student Course Drop")
root.geometry('320x200')

# Labels
lbl1 = Label(root, text = "Enter Student ID")
lbl2 = Label(root, text = "Enter Course ID")
lbl3 = Label(root, text = "Course Drop Pending")

lbl1.grid(row = 1, column = 0, padx = 10, pady = 10) 
lbl2.grid(row = 2, column = 0, padx = 10, pady = 10)
lbl3.grid(row = 5, column = 0, padx = 10, pady = 10)

# Fields
sid_field = Entry(root) 
cid_field = Entry(root)

sid_field.grid(row = 1, column = 1, padx = 10, pady = 10) 
cid_field.grid(row = 2, column = 1, padx = 10, pady = 10)
	
# Buttons
#Drop
btn_reg = Button(root, text = "Drop Course", fg = "red", command=clicked)
btn_reg.grid(row = 5, column = 1)

#Clear
btn_clr = Button(root, text = "Clear Entries", fg = "black", command = clear_all)
btn_clr.grid(row = 6, column = 1, pady = 10)


root.mainloop()
