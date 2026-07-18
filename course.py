class Course:

    def __init__(self,course_code, course_name):
        self.course_code = course_code
        self.course_name = course_name
        self.students = []
        self.assessments = []


    def add_student(self,student_id):
        if student_id not in self.students:
            self.students.append(student_id)
            print(f"{student_id} added to course!")
        else:
            print("student already added!")

    def remove_student(self,student_id):
        if student_id in self.students:
            self.students.remove(student_id)
            print(f"{student_id} removed from course!")

        else:
            print("student not Found!")


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
        print("Enrolled Students:", len(self.students))
        print("Assessments:")
        for assessment in self.assessments:
            assessment.display_info()


