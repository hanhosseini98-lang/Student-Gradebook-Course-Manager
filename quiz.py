from Assessment import Assessment

#1ST CHILD CLASS:

class Quiz(Assessment):

    def grade_message(self, score):
        percentage = self.calculate_percentage(score)

        if percentage >= 80:
            return "Good Job... Great Quiz Result!"
        elif percentage >= 50:
            return "Good Job... You Passed The Quiz!"
        elif percentage >= 30:
            return "Keep Studying!"
        else:
            return "Needs More Practice!"



    def display_info(self):
        print("===== Quiz Information =====")
        print(f"Quiz Title: {self.title} - Max Score: {self.max_score} ")

