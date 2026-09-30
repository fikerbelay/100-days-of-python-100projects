from quiz_brain import ProcessQuestion
process = ProcessQuestion()


class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    #def Ask(self, number):
     #   user_answer = input(f"Q.{number}: {self.question} (True/Fasle): ")
      #  process.check_answer(user_answer, self.answer)
