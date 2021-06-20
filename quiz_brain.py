from question_model import Question
from talk import Talk

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        print(f"Q:{self.question_number} - {current_question.text}", end=" ")
        Talk(current_question.text)
        user_answer = input(" (True/False)?: ")
        self.check_answer(current_question.answer, user_answer)
        print()


    # check is there any question left
    def is_quiz_still_on(self):
        return self.question_number < len(self.question_list)



    def check_answer(self, current_answer, user_answer):
        if current_answer[0].lower() == user_answer[0].lower():
            print("Thats right! Good answer.")
            self.score += 1
        else:
            print("Nope, You are wrong ;( ")
        # print score
        print(f"Your score: {self.score}/{self.question_number}")
