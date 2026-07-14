class course:

    def __init__(self,course_code, course_name, students, assessments):
        self.course_code = course_code
        self.course_name = course_name
        self.students = [30055678, 600200 ]
        self.assessments = []


    def add_student(self,student_id):
        if student_id not in self.students:
            self.students.append(student_id)
            print(f"{student_id} added to course!")
        else:
            print("student already added!")


    def add_assessment(self,assessment):
        if assessment not in self.assessments:
            self.assessments.append(assessment)
        else:
            print("assessment already added!")

    def find_assessment(self, title):
        for assessment in self.assessments:
            if assessment.title == title:
                return assessment
        else:
            return None

    def display_info(self):
        print("Course Code:", self.course_code)
        print("Course Name:", self.course_name)
        print("Enrolled Students:", self.students)
        print("Assessments:", self.assessments)


#TESTING THE "COURSE" CLASS:

course1 = course("12345", "Python Programming", [30055678], ["Quiz1: 70"])
course1.display_info()