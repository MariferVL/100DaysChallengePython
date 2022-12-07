from tkinter import *
import pandas as pd
from random import randint

# TODO If answer is correct save in file to count them
# TODO If answer is wrong save in file to show them at the end
def_displayed = []
checked_words = []
words_study = []
fav_words = []
data_dict = {}
item_def = ""
item_word = ""
item_type = ""
item_sentence = ""
num_words = 0
num_x = 0


def read_data():
    global data_dict
    try:
        data = pd.read_csv('Data/words_to_check.csv')
    except FileNotFoundError:
        data = pd.read_csv("Data/IELTS-Wordlist.csv")
    finally:
        data_dict = data.to_dict()
    return random_def(data_dict)

# TODO Change definitions
def random_def(data):
    global item_def, item_word, item_type, item_sentence
    start_button.destroy()
    if num_words + num_x < 90:
        i = randint(1, 91)
        item_def = data["definition"][i]
        item_word = data["word"][i]
        item_type = data["type"][i]
        item_sentence = data["sentence"][i]
        canvas.itemconfig(def_box, text=item_def)

        def_displayed.append({"Word": item_word, "Type": item_type, "Definition": item_def, "Sentence": item_sentence})

    else:
        canvas.create_image(0, 0, image=game_over)

    root.after(2000, show_answer)


def check_answer():
    global num_words
    checked_words.append(item_word)
    num_words = len(checked_words)
    count_check.delete('1.0', END)
    count_check.insert('end', f"{num_words}")
    clean_screen()
    random_def(data_dict)


def wrong_answer():
    global num_x
    words_study.append({"Word": item_word, "Type": item_type, "Definition": item_def, "Sentence": item_sentence})
    num_x = len(words_study)
    count_x.delete('1.0', END)
    count_x.insert('end', f"{num_x}")
    data = pd.DataFrame(words_study)
    # Append data
    data.to_csv('Data/words_to_check.csv', mode='a')
    clean_screen()
    random_def(data_dict)


# TODO Display answer
def show_answer():
    # word_key = list(item_def.keys())[list(item_def.values()).index(item_def)]
    canvas.itemconfig(type_word, text=item_type)
    root.after(2000, canvas.itemconfig(sentence_word, text=f"'{item_sentence}'"))
    root.after(4000, canvas.itemconfig(correct_answer, text=item_word.capitalize()))


##Working
def clean_screen():
    canvas.itemconfig(correct_answer, text="")
    canvas.itemconfig(type_word, text="")
    canvas.itemconfig(sentence_word, text="")


# TODO Save in file fav words
def save_fav():
    fav_words.append({"Word": item_word, "Type": item_type, "Definition": item_def, "Sentence": item_sentence})
    data = pd.DataFrame(fav_words)
    # data.to_csv("words_to_check.csv")
    # Append data
    data.to_csv('Data/favorite_words.csv', mode='a')


# TODO Create a reverse button

def reverse():
    last_def = def_displayed[-1]
    clean_screen()
    canvas.itemconfig(def_box, text=last_def["Definition"])
    canvas.itemconfig(correct_answer, text=last_def["Word"])
    canvas.itemconfig(type_word, text=last_def["Type"])
    canvas.itemconfig(sentence_word, text=f"'{last_def['Sentence']}'")


### UI Setup ###

# create GUI Main window
root = Tk()
root.title("Lexinger")
# root.wm_attributes('-transparentcolor', '#ab23ff')

# Adjust size:
root.geometry("363x600")
root.maxsize(363, 600)

# Add image file
bg = PhotoImage(file="Images/flash_card1.png")
game_over = PhotoImage(file="Images/flash_card2.png")

# create canvas to set flash card
canvas = Canvas(root, width=363, height=100)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg, anchor="nw")

# TODO Display meaning in screen
correct_answer = canvas.create_text(74, 127, anchor="nw", width=244, fill="#FF3D74", text="", font='"Klee One" 18 bold')
type_word = canvas.create_text(74, 160, anchor="nw", width=244, fill="#07B31C", text="", font='"Klee One" 12')
def_box = canvas.create_text(74, 188, anchor="nw", width=244, fill="#FF3D74", text="", font='"Klee One" 14 bold')
sentence_word = canvas.create_text(74, 277, anchor="nw", width=230, fill="#07B31C", text="",
                                   font='"Klee One" 11 italic')
count_x = Text(root, borderwidth=0, height=1, width=2, fg="#DBDBDB", wrap=WORD, font='Helvetica 13 bold')
count_x.place(x=266, y=383)
count_check = Text(root, borderwidth=0, fg="#DBDBDB", height=1, width=2, wrap=WORD, font='Helvetica 13 bold')
count_check.place(x=326, y=382)

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
start_button = Button(root, image=start_img, height=113, width=248, borderwidth=0,
                      command=read_data, relief="flat")
canvas.create_window(56, 170, window=start_button)
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
