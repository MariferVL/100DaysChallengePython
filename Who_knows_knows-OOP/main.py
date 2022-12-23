from trivia_model import Question
from data import triviaData
from trivia_constructor import Trivia


item_displayed = []
item_text = ""

for item in triviaData:
    item_question = item["question"]
    item_answer = item["correct_answer"]
    new_item = Question(item_question, item_answer)
    item_displayed.append(new_item)

quiz = Trivia(item_displayed)
root = TriviaUI()


# f"Your final score was: {quiz.score}/{quiz.question_number}"


