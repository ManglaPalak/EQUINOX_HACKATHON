PROBLEM STATEMENT:

Build a STUDENT RESULT MANAGEMENT SYSTEM for IGDTUW.

BRIEF ABOUT THE PROJECT

This is a MENU-DRIVEN user-friendly program written in PYTHON with MYSQL library. In this program, user can create, display, update and delete data from different tables. It deals with course details, student information and student scores and it can display student report cards as well. This code calculates total marks, percentage and grade of the students. By using MYSQL, it makes the representation of data very organized and presentable. The code has used many concepts of python like user-defined functions, list, etc.

HOW TO USE THE PROGRAM:

Since this project is a menu-driven program, so a menu will be displayed asking for your choice. The main menu contains the options:

STUDENT RECORD
COURSE RECORD
EXAM RECORD
REPORT CARD OF STUDENTS
EXIT THE PROGRAM
In Student Record option, you can see a sub-menu which contains the options:
Create
Display
Update
Delete
You will be asked for your choice. If you choose CREATE then you will be able to create a new data which will be added to the STUDENT_INFO table using query of MYSQL. On choosing DISPLAY we can either display all the records present in the table or we can also display a particular data from the table. For UPDATE, we can modify any data of any student in the table. Lastly, DELETE option will allow you to delete a particular record/data from the table.
Similarly for COURSE RECORD and EXAM RECORD options. COURSE RECORD deals with the course_data table and EXAM RECORD deals with student_record table in MYSQL with same options create, display, update and delete. Last but not the least, the program can print report card for each student separately. It is a user-friendly program and easy to understand.
REQUIREMENTS TO RUN THE PROGRAM:

1.mysql.connector-python must be downloaded in the computer.
2. python running application like jupyter notebook or IDLE should be present in the computer to run the program.
3. database and tables show be created in the mysql before running the program.
DATABASE STATEMENT:
"create database IGDTUW;"
TABLE STATEMENTS:

"create table student_info (admno int, name varchar(30), father_name varchar(30), mother_name varchar(30), mobile_no int, address varchar(30), category varchar(10))"
"create table course_data (course varchar(30), sub1 varchar(30), sub2 varchar(30), sub3 varchar(30), sub4 varchar(30), sub5 varchar(30), sub6 varchar(30), c_code varchar(8))"
"create table student_info (adm_no int, name varchar(30), course varchar(30), sub1 int, sub2 int, sub3 int, sub4 int, sub5 int, sub6 int, total int, percentage int, attendance int, grade varchar(3))"
