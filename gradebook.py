
class Gradebook:

    def __init__(self, passing_grade):
        self.students= {}
        self.courses = {}
        self.grades = {}
        self.passing_grade= passing_grade

    def add_student(self, student):
        if student.id in self.students:
            print("Student already Exists!")
            return False

        self.students[student.id] = student
        print("Student added successfully!")
        return True

    def add_course(self, course):
        if course.course_code in self.courses:
            print("Course already Exists!")
            return False
        self.courses[course.course_code] = course
        print("Course added successfully!")
        return True

    def enroll_student(self, student_id, course_code):
        if student_id not in self.students:
            return False

        if course_code not in self.courses:
            return False

        student = self.students[student_id]
        course = self.courses[course_code]

        student.enroll_course(course_code)
        course.add_student(student_id)
        return True

    def add_assessment(self, course_code, assessment):
        if course_code not in self.courses:
            return False

        course = self.courses[course_code]
        course.add_assessment(assessment)
        return True

    def record_grade(self, student_id, course_code, assessment_title, score):
        if student_id not in self.students:
            return False

        if course_code not in self.courses:
            return False

        course= self.courses[course_code]

        found_assessment = None

        for assessment in course.assessments:
            if assessment_title == assessment.title:
                found_assessment = assessment
                break

        if found_assessment is None:
           return False

        score = float(score)

        if score < 0 or score >found_assessment.max_score:
            print("Invalid Score!")
            return False

        if student_id not in self.grades:
            self.grades[student_id] = {}

        if course_code not in self.grades[student_id]:
            self.grades[student_id][course_code] = {}

        self.grades[student_id][course_code][assessment_title] = float(score)
        return True

    def calculate_average(self, student_id, course_code):
        if student_id not in self.students:
            return False
        if course_code not in self.courses:
            return False

        if student_id not in self.grades:
            return False
        if course_code not in self.grades[student_id]:
            return False

        if len(self.grades[student_id][course_code]) == 0:
            return False

        total_score = 0
        for grade in self.grades[student_id][course_code].values():
            total_score += grade

        average = total_score / len(self.grades[student_id][course_code])
        return round(average,2)

    def show_report(self, student_id):
        print("==== Student Report ====")
        if student_id not in self.students:
            print("Student ID not found!")
            return

        student = self.students[student_id]
        student.display_info()

        for course_code in student.courses:
            course = self.courses[course_code]
            course.display_info()

            average= self.calculate_average(student_id, course_code)

            if average is not False:
               print("Average:", average)
               print("Letter Grade:", self.get_letter_grade(average))
               print("Result:", self.get_result(average))
            else:
               print("Average: No Grades Recorded!")

    def search_student(self,keyword):

        for student in self.students.values():
            if keyword.lower() in student.id.lower() or keyword.lower() in student.name.lower():
                return student

        return None

    def delete_student(self,student_id):
        if student_id not in self.students:
            print("Student ID not found!")
            return
        student = self.students[student_id]

        for course_code in student.courses:
            course = self.courses[course_code]
            course.remove_student(student_id)

        if student_id in self.grades:
            del self.grades[student_id]

        del self.students[student_id]
        print("Student Deleted Successfully!")

    def get_result(self, average):
        if average >= self.passing_grade:
            return "Passed!"

        return "Failed!"

#CREATIVE METHODS:
    def get_letter_grade(self, average):

        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

    def show_dashboard(self):
        total_students = len(self.students)
        total_courses = len(self.courses)
        total_assessments = 0
        for course in self.courses.values():
            total_assessments += len(course.assessments)

        print("Total Students:", total_students)
        print("Total Courses:", total_courses)
        print("Total Assessments:", total_assessments)