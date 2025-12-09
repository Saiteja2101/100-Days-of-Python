
class Quiz:

    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.game_over = False


    def next_question(self):
        while not self.game_over and self.question_number < len(self.question_list):
            current_question = self.question_list[self.question_number]
            user_answer= input(f"Q.{self.question_number + 1}, {current_question.text} (True/False): ")
            if user_answer == current_question.answer:
                self.question_number += 1
            else:
                print(f"Game Over! You have lost your score is {self.question_number} ")
                self.game_over = True
            
        if self.question_number == len(self.question_list):
            print("Congratulations! You finished all questions!")
            self.game_over = True

