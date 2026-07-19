#PARENT CLASS:

class Assessment:
    def __init__(self, title, max_score):
        self.title = title
        self.max_score = int(max_score)

#THE STUDENT SCORE TURNS INTO PERCENTAGES:
    def calculate_percentage(self, score):
        return round((score/self.max_score)*100, 2)

#USE THE PERCENTAGE METHOD TO SHOW A MESSAGE:
    def grade_message(self, score):
        percentage = self.calculate_percentage(score)

        if percentage >= 80:
            return "Good Job... Great Score!"
        elif percentage >= 50:
            return "Good Job... You Passed!"
        elif percentage <= 30:
            return "You Failed...!"
        else:
            return "Needs Improvement!"


    def display_info(self):
        print("====Assessment Information====")
        print("Title:", self.title)
        print("Max Score:", self.max_score)
