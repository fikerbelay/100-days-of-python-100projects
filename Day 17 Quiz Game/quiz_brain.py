import question_model
from data import question_data




class ProcessQuestion:
    def __init__(self):
        self.number = 0

    def fetch(self):
        for q_and_a in question_data:
            self.number += 1
            question = q_and_a['text']
            answer = q_and_a['answer']
            qua = question_model.Question(question, answer)
            #qua.Ask(self.number)

  #  def check_answer(self, u_answer, answer):
   #     if u_answer == answer:
    #        print("correct")