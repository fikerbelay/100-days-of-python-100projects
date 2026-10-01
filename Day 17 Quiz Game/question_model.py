class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def Ask(self, number):
        user_answer = input(f"Q.{number}: {self.question} (True/Fasle): ")
        return user_answer.capitalize()