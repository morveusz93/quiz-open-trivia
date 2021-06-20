import html


class Question:
    def __init__(self, question):
        self.text = html.unescape(question["question"])
        self.answer = question["correct_answer"]