from Assessment import Assessment

#2ND CHILD CLASS:

class Exam(Assessment):

    def grade_message(self, score):
        percentage = self.calculate_percentage(score)

        if percentage >= 55:
            return "Good Job... You Passed The Exam!"
        else:
            return "You Failed The Exam!"

    def display_info(self):
        print("===== Exam Information =====")
        print(f"Exam Title: {self.title} - Max Score: {self.max_score} ")
