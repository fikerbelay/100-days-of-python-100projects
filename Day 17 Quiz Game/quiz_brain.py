import question_model
from data import question_data


class ProcessQuestion:
    def __init__(self):
        self.number = 0
        self.score = 0

    def fetch(self):

        for q_and_a in question_data:

            self.number += 1
            question = q_and_a['text']
            answer = q_and_a['answer']
            qua = question_model.Question(question, answer)
            u_answer = qua.Ask(self.number)

            self.check_answer(u_answer, answer)


    def check_answer(self, u_answer, answer):
        if u_answer == answer:
            self.score += 1
            print("You got it right!")
            print(f"The correct answer was: {answer}.")
            print(f"Your current score is: {self.score} / {self.number}")
        else:
            print("That's wrong")
            print(f"The correct answer was: {answer}.")
            print(f"Your current score is: {self.score} / {self.number}")