class Student:

    def __init__(self,id, name,email):
        self.id = id
        self.name = name
        self.email = email
        self.courses = []


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


    def enroll_course(self, course_code):
        self.courses.append(course_code)

    def display_info(self):
       print("Student ID:", self.id)
       print("Name:", self.name)
       print("Email:", self.email)
       print("Courses:", self.courses)





