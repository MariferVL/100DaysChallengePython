from tkinter import *
import pandas as pd
from random import randint

# TODO If answer is correct save in file to count them
# TODO If answer is wrong save in file to show them at the end
checked_words = []
unknown_words = []
fav_words = []
dictionary = pd.read_csv("Data/IELTS-Wordlist.csv")
data_dict = dictionary.to_dict()
item = ""
words_studied = []
num_words = 0
num_x = 0


# TODO Change definitions
def random_def():
    global item
    start_button.destroy()
    def_box.delete('1.0', END)
    i = randint(0, 90)
    if num_words + num_x < 91:
        item = data_dict["definition"][i]
        words_studied.append(item)
        def_box.insert('end', item)

        # if item not in checked_words and item not in unknown_words:
    else:
        game_over = "Has revisado todas las palabras"
        def_box.insert('end', game_over)
    root.after(4400, show_answer)


def check_answer():
    global num_words
    checked_words.append(item)
    num_words = len(checked_words)
    count_check.delete('1.0', END)
    correct_answer.delete('1.0', END)
    count_check.insert('end', f"{num_words}")
    random_def()


def wrong_answer():
    global num_x
    unknown_words.append(item)
    num_x = len(unknown_words)
    count_x.delete('1.0', END)
    correct_answer.delete('1.0', END)
    count_x.insert('end', f"{num_x}")
    random_def()
    print("Guardado para estudiar!")


# TODO Display answer
def show_answer():
    def_dict = data_dict["definition"]
    word_dict = data_dict["word"]
    word_key = list(def_dict.keys())[list(def_dict.values()).index(item)]
    correct_answer.insert('end', f"{(word_dict[word_key]).capitalize()}")


# TODO Save in file fav words
def save_fav():
    fav_words.append(item)


# TODO Create a reverse button

def reverse():
    last_def = words_studied[-2]
    def_box.delete('1.0', END)
    def_box.insert('end', last_def)



df_dict = pd.DataFrame(squirrel_dict)
df_dict.to_csv("squirrel_count.csv")

### UI Setup ###

# create GUI Main window
root = Tk()
root.title("Lexinger")

# Adjust size:
root.geometry("363x600")
# Add image file
bg = PhotoImage(file="Images/flash_card.png")

# create canvas to set flash card
canvas = Canvas(root, width=363, height=600)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg, anchor="nw")

# TODO Display meaning in screen
def_box = Text(root, height=6, width=16, borderwidth=0, bg="black", fg="white",
               font='"Klee One" 16 bold', wrap=WORD)
def_box.place(x=72, y=150)
count_x = Text(root, borderwidth=0, height=1, width=2, fg="#DBDBDB", wrap=WORD, font='Helvetica 13 bold')
count_x.place(x=266, y=383)
count_check = Text(root, borderwidth=0, fg="#DBDBDB", height=1, width=2, wrap=WORD, font='Helvetica 13 bold')
count_check.place(x=326, y=382)
correct_answer = Text(root, borderwidth=0, height=1, width=22, fg="black", wrap=WORD, font='"Klee One" 16 bold')
correct_answer.place(x=44, y=411)
# correct_answer.delete('1.0', END)

# Number of Words guessed

# TODO Create fav, correct, wrong and reverse buttons.
# Buttons img
start_img = PhotoImage(file="Images/start-button.png")
x_img = PhotoImage(file="Images/x_btn.png")
x_img = x_img.zoom(13)
x_img = x_img.subsample(33)
check_img = PhotoImage(file="Images/like_btn.png")
check_img = check_img.zoom(11)
check_img = check_img.subsample(33)
fav_img = PhotoImage(file="Images/fav_btn.png")
fav_img = fav_img.zoom(6)
fav_img = fav_img.subsample(33)
reverse_img = PhotoImage(file="Images/back_button.png")
reverse_img = reverse_img.zoom(6)
reverse_img = reverse_img.subsample(33)

# Buttons UI
start_button = Button(root, image=start_img, height=113, width=248, activebackground='black', borderwidth=0,
                      command=random_def)
start_button.place(x=56, y=170)
Button(root, image=x_img, height=44, width=44, borderwidth=0, command=wrong_answer).place(x=114, y=502)
Button(root, image=check_img, height=44, width=44, borderwidth=0, command=check_answer).place(x=203, y=503)
Button(root, image=fav_img, height=29, width=29, borderwidth=0, command=save_fav).place(x=282, y=493)
Button(root, image=reverse_img, height=29, width=29, borderwidth=0, command=reverse).place(x=52, y=493)

# # Track Mouse Position:
# def motion(event):
#     x, y = event.x, event.y
#     print('{}, {}'.format(x, y))
#
#
# root.bind('<Motion>', motion)

# start the GUI
root.mainloop()
