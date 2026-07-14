class Student:

    def __init__(self,id, name,email):
        self.id = id
        self.name = name
        self.email = email
        self.courses = ["MAT1212"]


    def get_id(self):
        return self.id

    def get_name(self):
       return self.name

    def set_email(self, email):
        if "@" not in email and "." not in email or " " in email:
            self.email = email
            print("Invalid email Address!")
            return False

        else:
            print("The Email Address is updated1")
            return True


    def enroll_courses(self, course_code):
        self.courses.append(course_code)

    def display_info(self):
       print("Student ID:", self.id)
       print("Name:", self.name)
       print("Email:", self.email)
       print("Courses:", self.courses)

#TESTING THE CODES! HOPE IT WORKS PROPERLY.

student1= Student("30055678","Hanieh Hosseini","hanhosseini98@gmail.com")

student1.enroll_courses("ITI1101")
student1.display_info()



