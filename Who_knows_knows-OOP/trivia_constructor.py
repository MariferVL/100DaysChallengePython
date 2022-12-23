from html import unescape


class Trivia:

    def __init__(self, q_list):
        self.question_number = 0
        self.answer = ""
        self.score = 0
        self.wrong = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        text = unescape(self.current_question.text)
        return text

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            self.wrong += 1
            print("That's wrong.")
