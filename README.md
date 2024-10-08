# JCU-SIS

This application is a mock John Carroll University Student Information System. It uses Python GUIs combined with SQL code to select, insert, and delete information from a database in SQLiteStudio.

Functionalities include:
- Data Entry: adding a student, instructor, or course to the database
- Course Registration: registering or dropping a student from a course
- Reports: selecting and printing out the student or instructor schedules

The main dashboard functions as the hub for all activity.
<br>
![main_dashboard](https://github.com/user-attachments/assets/78369e5b-449b-41d7-9641-fda8a0918776)


Data entry allows you to add a student, instructor, or course to the database. Clicking one of the buttons will bring up another GUI to enter in the data.
<br>
This is the Add Student GUI:
<br>
![add_student](https://github.com/user-attachments/assets/5f9f1030-157f-4c8f-aff1-22adc7626a3b)
<br>
Pressing "Add Student" will add the information straight into the database.


Course Registration allows a student to be added to or dropped from a class. This is data is stored in a separate StudentCourse table in the database.
<br>
![course_registration](https://github.com/user-attachments/assets/7c30acca-430c-4dc2-82d0-98101956e6e5)


Reports can print out schedules. These schedules only include the students that are enrolled in a course, or instructors that are scheduled to teach a course.
<br>
These schedules are pulled from the database and printed out.
<br>

Students Schedule:
<br>
![sroster_1](https://github.com/user-attachments/assets/4ddca723-4926-4193-b8d7-a7afd9b4d6b0)
<br>

Instructor Schedule:
<br>
![iroster_2](https://github.com/user-attachments/assets/cd1f3559-ab22-42dc-9762-8da2fc2a228e)

