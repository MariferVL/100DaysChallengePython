class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score= 0

    def still_have_q(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        item = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q{self.question_number}: {item.text} (True/False)?: ").capitalize()
        self.check_answer(answer, item.answer)

    def check_answer(self, user_answer, correct_answer ):
        if user_answer == correct_answer:
            self.score += 1
            print("Correct! Well done.👏")

        else:
            print("Wrong answer 🙁 ")
        self.final_score()
        print("\n")

    def final_score(self):
        print(f" Your current score is: {self.score}/{self.question_number}")

