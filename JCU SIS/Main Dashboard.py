#Main Dashbard of SIS

from tkinter import *

###Functions
# Data Entry
#opens add student GUI when btn_sudent is clicked
def addStudent():
    import GUI_for_Add_Student
#opens add instructor GUI when btn_instructor is clicked
def addInstructor():
    import GUI_for_Add_Instructor
#opens add course GUI when btn_course is clicked
def addCourse():
    import GUI_for_Add_Course

# Course Registration
#opens course registration GUI when btn_register is clicked
def registerCourse():
    import GUI_for_Course_Registration
#opens course drop GUI when btn_drop is clicked
def dropCourse():
    import GUI_for_Course_Drop

# Reports
#runs sroster that displays the student schedules when btn_studentSchedule is clicked
def sroster():
    import SELECT_sis_db_2700_sroster
#runs iroster that displays the instructor rosters when btn_insrtuctorRoster is clicked
def iroster():
    import SELECT_sis_db_2700_iroster


###GUI
# GUI Creation
root = Tk()
root.title("JCU Student Information System")
root.geometry('500x200')

# Labels
lbl1 = Label(root, text = "Data Entry", font = "bold")
lbl2 = Label(root, text = "Course Registration", font = "bold")
lbl3 = Label(root, text = "Reports", font = "bold")

lbl1.grid(row = 1, column = 0, padx = 20, pady = 5) 
lbl2.grid(row = 1, column = 1, padx = 20, pady = 10)
lbl3.grid(row = 1, column = 2, padx = 20, pady = 10)

# Buttons
#Add Student
btn_student = Button(root, text = "Student", command = addStudent)
btn_student.grid(row = 2, column = 0, padx = 10, pady = 5)
#Add Instructor
btn_instructor = Button(root, text = "Instructor", command = addInstructor)
btn_instructor.grid(row = 3, column = 0, padx = 10, pady = 5)
#Add Course
btn_course = Button(root, text = "Course", command = addCourse)
btn_course.grid(row = 4, column = 0, padx = 10, pady = 5)

#Add
btn_register = Button(root, text = "Register for Course", command = registerCourse)
btn_register.grid(row = 2, column = 1, padx = 10, pady = 5)
#Drop
btn_drop = Button(root, text = "Drop a Course", command = dropCourse)
btn_drop.grid(row = 3, column = 1, padx = 10, pady = 5)

#Student Schedule
btn_studentSchedule = Button(root, text = "Student Schedules", command = sroster)
btn_studentSchedule.grid(row = 2, column = 2, padx = 10, pady = 5)
#Instructor Roster
btn_insrtuctorRoster = Button(root, text = "Instructor Rosters", command = iroster)
btn_insrtuctorRoster.grid(row = 3, column = 2, padx = 10, pady = 5)


root.mainloop()
