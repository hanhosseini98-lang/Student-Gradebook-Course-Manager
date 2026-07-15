#PARENT CLASS:

class Assessment:
    def __init__(self, title, max_score):
        self.title = title
        self.max_score = max_score

#THE STUDENT SCORE TURNS INTO PERCENTAGES:
    def calculate_percentage(self, score):
        return (score/self.max_score)*100

#USE THE PERCENTAGE METHOD TO SHOW A MESSAGE:
    def grade_message(self, score):
        percentage = self.calculate_percentage(score)

        if percentage >= 80:
            return "Good Job... Great Score!"
        elif percentage >= 50:
            return "Good Job... You Passed!"
        elif percentage <= 30:
            return "Needs Improvement!"
        else:
            return "You Failed...!"


    def display_info(self):
        print("Title:", self.title)
        print("Max Score:", self.max_score)


#TESTING THE CODE! HOPE IT WORKS PROPERLY!

quiz = Assessment("Python Quiz", 70)
quiz.display_info()
print(quiz.calculate_percentage(20))
print(quiz.grade_message(30))