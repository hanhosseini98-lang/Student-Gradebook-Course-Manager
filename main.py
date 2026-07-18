from course import Course
from student import Student
from Assessment import Assessment
from gradebook import Gradebook
from quiz import Quiz
from exam import Exam
from project import Project

gradebook = Gradebook(55)

while True:

  print("""
   ====Student GradeBook Manager====
   1. Add Student
   2. View Students
   3. Add Course
   4. Enroll Student in Course
   5. Add Assignment
   6. Record Grade
   7. View Student Report
   0. Exit
   
   Choose an Option:
   """)

  choice = input("Choose your Option: ")

  if choice == "0":
      break


  elif choice == "1":
      id = input("Enter your ID: ")
      name = input("Enter your name: ")
      email = input("Enter your email: ")
      student = Student(id, name, email)
      gradebook.add_student(student)


  elif choice == "2":
      if not gradebook.students:
          print("No student Found!")
      else:
          for student in gradebook.students.values():
              student.display_info()


  elif choice == "3":
      course_code = input("Enter your course code: ")
      course_name = input("Enter your course name: ")
      course = Course(course_code, course_name)
      gradebook.add_course(course)


  elif choice == "4":
      student_id = input("Enter your student ID: ")
      course_course = input("Enter your course Code: ")
      if gradebook.enroll_student(student_id, course_course):
          print("Student Enrolled Successfully!")
      else:
          print("Enrollment Failed!")


  elif choice == "5":
      course_code = input("Enter course code: ")
      title = input("Enter Assessment title: ")
      max_score = input("Enter maximum score: ")

      assessment_type = input("Enter assessment type: ").lower()

      if assessment_type == "quiz":
          assessment = Quiz(title, max_score)
      elif assessment_type == "exam":
          assessment = Exam(title, max_score)
      elif assessment_type == "project":
          assessment = Project(title, max_score)
      else:
          print("Assessment Type Not Found!")
          continue

      if gradebook.add_assessment(course_code,assessment ):
          print("Assessment Added Successfully!")
      else:
          print("Assessment Type Not Found!")


  elif choice == "6":
      student_id = input("Enter your student ID: ")
      course_code = input("Enter your course code: ")
      assessment_title = input("Enter assessment title: ")
      score = float(input("Enter your score: "))

      if gradebook.record_grade(student_id, course_code, assessment_title, score):
         print("Grade Record Successfully!")
      else:
         print("Grade Record Not Found!")


  elif choice == "7":
      student_id = input("Enter your student ID: ")
      gradebook.show_report(student_id)

