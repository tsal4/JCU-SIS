#GUI for Adding a Student to the Database

import sqlite3
from tkinter import *

###Functions
# function for clearing the contents of all entry boxes 
def clear_all():
	sid_field.delete(0, END)
	firstName_field.delete(0, END)
	middleInitial_field.delete(0, END)
	lastName_field.delete(0, END)
	email_field.delete(0, END)
	rank_field.delete(0, END)
	major_field.delete(0, END)
	minor_field.delete(0, END)
	igs_field.delete(0, END)
	enrollType_field.delete(0, END)
	address_field.delete(0, END)
	state_field.delete(0, END)
	athlete_field.delete(0, END)
	advisor_field.delete(0, END)
	gpa_field.delete(0, END)
	honors_field.delete(0, END)
	aidEligibility_field.delete(0, END)

# function to display text when button is clicked
def clicked():
	lbl18.configure(text = "Student Added!")
	SQLinsert()

# SQL Insert function
def SQLinsert():
	sid_data = sid_field.get()
	firstName_data = firstName_field.get()
	middleInitial_data = middleInitial_field.get()
	lastName_data = lastName_field.get()
	email_data = email_field.get()
	rank_data = rank_field.get()
	major_data = major_field.get()
	minor_data = minor_field.get()
	igs_data = igs_field.get()
	enrollType_data = enrollType_field.get()
	address_data = address_field.get()
	state_data = state_field.get()
	athlete_data = athlete_field.get()
	advisor_data = advisor_field.get()
	gpa_data = gpa_field.get()
	honors_data = honors_field.get()
	aidEligibility_data = aidEligibility_field.get()
	sql = '''INSERT INTO student (sid, firstName, middleInitial, lastName, email, rank, major, minor, igs, 
									enrolltype, address, state, athlete, advisor, gpa, honors, aidEligibility) 
			VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
	c.execute(sql, (sid_data, firstName_data, middleInitial_data, lastName_data, email_data, rank_data, major_data, minor_data, igs_data, 
				 		enrollType_data, address_data, state_data, athlete_data, advisor_data, gpa_data, honors_data, aidEligibility_data))
	conn.commit()


###SQL
# connect to our database
conn = sqlite3.connect("C:\CS 2700 51\CS 2700 DB\sis_db_2700_2")

# define cursor
c = conn.cursor()


###GUI 
# GUI Creation
root = Tk()
root.title("Add Student")
root.geometry('350x800')

# Labels
lbl1 = Label(root, text = "Enter Student ID")
lbl2 = Label(root, text = "Enter First Name")
lbl3 = Label(root, text = "Enter Middle Initial")
lbl4 = Label(root, text = "Enter Last Name")
lbl5 = Label(root, text = "Enter Email")
lbl6 = Label(root, text = "Enter Rank (FR, SO, JR, SR, GR)")
lbl7 = Label(root, text = "Enter Major")
lbl8 = Label(root, text = "Enter Minor")
lbl9 = Label(root, text = "In Good Standing (Y/N)")
lbl10 = Label(root, text = "Enrollment Type (FT/PT)")
lbl11 = Label(root, text = "Enter Address")
lbl12 = Label(root, text = "Enter State")
lbl13 = Label(root, text = "Athlete (Y/N)")
lbl14 = Label(root, text = "Enter Advisor Name")
lbl15 = Label(root, text = "Enter GPA")
lbl16 = Label(root, text = "Honors (Y/N)")
lbl17 = Label(root, text = "Aid Eligible (Y/N)")
lbl18 = Label(root, text = "Pending")

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
lbl11.grid(row = 11, column = 0, padx = 10, pady = 10)
lbl12.grid(row = 12, column = 0, padx = 10, pady = 10)
lbl13.grid(row = 13, column = 0, padx = 10, pady = 10)
lbl14.grid(row = 14, column = 0, padx = 10, pady = 10)
lbl15.grid(row = 15, column = 0, padx = 10, pady = 10)
lbl16.grid(row = 16, column = 0, padx = 10, pady = 10)
lbl17.grid(row = 17, column = 0, padx = 10, pady = 10)
lbl18.grid(row = 18, column = 0, padx = 10, pady = 10)

# Fields
sid_field = Entry(root)
firstName_field = Entry(root)
middleInitial_field = Entry(root)
lastName_field = Entry(root)
email_field = Entry(root)
rank_field = Entry(root)
major_field = Entry(root)
minor_field = Entry(root)
igs_field = Entry(root)
enrollType_field = Entry(root)
address_field = Entry(root)
state_field = Entry(root)
athlete_field = Entry(root)
advisor_field = Entry(root)
gpa_field = Entry(root)
honors_field = Entry(root)
aidEligibility_field = Entry(root)

sid_field.grid(row = 1, column = 1, padx = 10, pady = 10) 
firstName_field.grid(row = 2, column = 1, padx = 10, pady = 10)
middleInitial_field.grid(row = 3, column = 1, padx = 10, pady = 10)
lastName_field.grid(row = 4, column = 1, padx = 10, pady = 10)
email_field.grid(row = 5, column = 1, padx = 10, pady = 10)
rank_field.grid(row = 6, column = 1, padx = 10, pady = 10)
major_field.grid(row = 7, column = 1, padx = 10, pady = 10)
minor_field.grid(row = 8, column = 1, padx = 10, pady = 10)
igs_field.grid(row = 9, column = 1, padx = 10, pady = 10)
enrollType_field.grid(row = 10, column = 1, padx = 10, pady = 10)
address_field.grid(row = 11, column = 1, padx = 10, pady = 10)
state_field.grid(row = 12, column = 1, padx = 10, pady = 10)
athlete_field.grid(row = 13, column = 1, padx = 10, pady = 10)
advisor_field.grid(row = 14, column = 1, padx = 10, pady = 10)
gpa_field.grid(row = 15, column = 1, padx = 10, pady = 10)
honors_field.grid(row = 16, column = 1, padx = 10, pady = 10)
aidEligibility_field.grid(row = 17, column = 1, padx = 10, pady = 10)

# Buttons
#Register
btn_reg = Button(root, text = "Add Student", fg = "red", command=clicked)
btn_reg.grid(row = 18, column = 1)

#Clear 
btn_clr = Button(root, text = "Clear Entries", fg = "black", command = clear_all)
btn_clr.grid(row = 29, column = 1, pady = 10)


root.mainloop()
