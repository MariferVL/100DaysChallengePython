from trivia_model import Question
from data import triviaData
from trivia_constructor import Trivia
from tkinter import *
from html import unescape

item_displayed = []
item_text = ""

for item in triviaData:
    item_question = item["question"]
    item_answer = item["correct_answer"]
    new_item = Question(item_question, item_answer)
    item_displayed.append(new_item)

quiz = Trivia(item_displayed)


# f"Your final score was: {quiz.score}/{quiz.question_number}"


def start_game():
    start_button.destroy()
    clean_screen()
    if quiz.still_has_questions():
        quiz.next_question()
        i_text = unescape(quiz.current_question.text)
        canvas.itemconfig(text_box, text=i_text)
    else:
        game_over()


def game_over():
    clean_screen()
    canvas.itemconfig(canvas_bg, image=game_over_img)


def press_false():
    quiz.check_answer("false")
    update_score()
    start_game()


def press_true():
    quiz.check_answer("true")
    update_score()
    start_game()


def update_score():
    count_check.delete('1.0', END)
    count_check.insert('end', f"{quiz.score}")
    count_x.delete('1.0', END)
    count_x.insert('end', f"{quiz.wrong}")


def clean_screen():
    canvas.itemconfig(text_box, text="")


### UI Setup ###

# create GUI Main window
root = Tk()
root.title("Who knows, knows.")
# root.wm_attributes('-transparentcolor', '#ab23ff')

# Adjust size:
root.geometry("363x600")
root.maxsize(363, 600)

# Add image file
bg = PhotoImage(file="images/flash_card1.png")
game_over_img = PhotoImage(file="images/flash_card2.png")

# create canvas to set flash card
canvas = Canvas(root, width=363, height=100)
canvas.pack(fill="both", expand=True)
canvas_bg = canvas.create_image(0, 0, image=bg, anchor="nw")

# Display question on screen
text_box = canvas.create_text(74, 181, anchor="nw", width=236, fill="#FF3D74", text="", font='"Klee One" 12 bold',
                              justify=LEFT)
count_check = Text(root, borderwidth=0, height=1, width=2, fg="#DBDBDB", wrap=WORD, font='Helvetica 13 bold')
count_check.place(x=326, y=386)

count_x = Text(root, borderwidth=0, fg="#DBDBDB", height=1, width=2, wrap=WORD, font='Helvetica 13 bold')
count_x.place(x=266, y=386)

# Buttons img
start_img = PhotoImage(file="images/start_button.png")
x_img = PhotoImage(file="images/x_btn.png")
x_img = x_img.zoom(13)
x_img = x_img.subsample(33)
check_img = PhotoImage(file="images/like_btn.png")
check_img = check_img.zoom(11)
check_img = check_img.subsample(33)

# Buttons UI
start_button = Button(root, image=start_img, borderwidth=0, height=113, width=248, command=start_game, relief="flat")
canvas.create_window(54, 168, anchor="nw", window=start_button)
Button(root, image=x_img, height=44, width=44, borderwidth=0, command=press_false).place(x=114, y=502)
Button(root, image=check_img, height=44, width=45, borderwidth=0, command=press_true).place(x=203, y=503)

# # Track Mouse Position:
# def motion(event):
#     x, y = event.x, event.y
#     print('{}, {}'.format(x, y))
#
# root.bind('<Motion>', motion)

# start the GUI
root.mainloop()
