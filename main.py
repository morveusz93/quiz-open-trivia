from question_model import Question
from quiz_brain import QuizBrain
from data import QuestionData



def main():
    data = QuestionData().questions_data
    if len(data) < 1:
        print("Sorry, we don't have enough questions in this category. Please chosse other one.")
        return main()
    question_bank = [Question(question) for question in data]
    quiz = QuizBrain(question_bank)

    while quiz.is_quiz_still_on():
        quiz.next_question()
    print()
    print("Congrats! It's the end of quiz!")
    print(f"Your score is: {quiz.score}/{quiz.question_number}")


if __name__ == "__main__":
    main()