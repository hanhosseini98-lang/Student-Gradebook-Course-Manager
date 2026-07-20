from Assessment import Assessment

#3RD CHILD CLASS:
class Project(Assessment):

    def grade_message(self, score):
        percentage = self.calculate_percentage(score)
        if percentage >= 70:
            return "Excellent Project!"
        elif percentage >= 40:
            return "Project Submitted!"
        else:
            return "Project Needs Improvement!"

    def display_info(self):
        print("===== Project Information =====")
        print(f"Project Title: {self.title} - Max Score: {self.max_score} ")

