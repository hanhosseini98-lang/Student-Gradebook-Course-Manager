# Student Gradebook & Course Manager

## Project Overview

The Student Gradebook & Course Manager is a terminal-based Python application developed as the final project for a Python programming course.

The application allows users to manage students, courses, assessments, and grades using Object-Oriented Programming (OOP).
It demonstrates the use of classes, inheritance, encapsulation, dictionaries, lists, and method overriding.

------------------------------------------------------------------------------------------------

## Features

* Add new students
* View all students
* Add new courses
* Enroll students in courses
* Add assessments (Quiz, Exam, Project)
* Record student grades
* Calculate course averages
* Generate student reports
* Determine pass/fail results
* look for student based on ID or name
* Remove Student From courses

### Custom Features

* Letter Grades: Converts numerical averages into letter grades (A, B, C, D, F).
* Dashboard: Displays the total number of students, courses, and assessments.

----------------------------------------------------------------------------------------------

## Project Structure

### Student

Stores student information, including:

* Student ID
* Name
* Email
* Enrolled courses

### Course

Stores:

* Course code
* Course name
* Enrolled students
* Assessments

### Assessment

Parent class representing graded work.

Child classes:

* Quiz
* Exam
* Project

Each child class overrides the grading behavior when needed.

### Gradebook

Acts as the main controller of the application by:

* Managing students and courses
* Recording grades
* Calculating averages
* Generating reports
* Displaying dashboard statistics

------------------------------------------------------------------------------------------------

## Technologies Used

* Python
* Object-Oriented Programming (OOP)

Python concepts demonstrated:

* Classes and Objects
* Encapsulation
* Inheritance
* Method Overriding
* Lists
* Dictionaries
* Functions
* Loops
* Conditional Statements

-------------------------------------------------------------------------------------------------

## Menu

===== Student Gradebook Manager =====

1. Add Student
2. View Students
3. Add Course
4. Enroll Student in Course
5. Add Assessment
6. Record Grade
7. View Student Report
8. Show Dashboard
9. Search Student
10. Remove Student
0. Exit
-------------------------------------------------------------------------------------------------

## Project Limitations

This project is terminal-based and does not include file handling or database storage. 
All data is stored in memory while the program is running.

--------------------------------------------------------------------------------------------------

## What I Learned

During this project, I practiced:
- Designing classes using OOP
- Working with dictionaries and lists
- Using inheritance and method overriding
- Building a menu-driven application
- Connecting multiple classes together



## Author

Hanieh Hosseini

Final Python Project – Student Gradebook & Course Manager
