class Student:

    def __init__(self,student_id, name,email):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.courses = []


    def get_id(self):
        return self.student_id

    def get_name(self):
       return self.name

    def set_email(self, email):

        if "@" not in email or "." not in email or " " in email:
            print("Invalid email Address!")
            return False

        self.email = email
        print("Email updated successfully!")
        return True


    def enroll_course(self, course_code):
        if course_code not in self.courses:
           self.courses.append(course_code)

    def display_info(self):
       print("Student ID:", self.id)
       print("Name:", self.name)
       print("Email:", self.email)

       if self.courses:
           print("Courses:")
           for course in self.courses:
               print("-",course)
       else:
            print("Courses; No Courses Enrolled!")



