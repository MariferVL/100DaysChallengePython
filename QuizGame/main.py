from question_model import *
from data import question_data
from quiz_brain import *

question_bank = []


for item in question_data:
    item_text = item["question"]
    item_answer = item["correct_answer"]
    new_question = Question(item_text,item_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_have_q():
    quiz.next_question()
print("You've completed the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")

