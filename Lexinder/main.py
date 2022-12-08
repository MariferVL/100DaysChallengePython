from tkinter import *
import pandas as pd
from random import randint

# TODO If answer is correct save in file to count them
# TODO If answer is wrong save in file to show them at the end
def_displayed = []
checked_words = []
words_study = []
fav_words = []
item_def = ""
item_word = ""
item_type = ""
item_sentence = ""
num_words = 0
num_x = 0
wait = ""
wait2 = ""

data = pd.read_csv("Data/IELTS-Wordlist.csv")
data_dict = data.to_dict()
print(data_dict)


# try:
#     data = pd.read_csv('Data/words_to_check.csv')
# except FileNotFoundError:
#     data = pd.read_csv("Data/IELTS-Wordlist.csv")
# finally:


# TODO Change definitions
def random_def():
    global item_def, item_word, item_type, item_sentence
    start_button.destroy()
    if num_words + num_x < 90:
        i = randint(1, 90)
        item_def = data_dict["definition"][i]
        item_word = data_dict["word"][i]
        item_type = data_dict["type"][i]
        item_sentence = data_dict["sentence"][i]
        canvas.itemconfig(def_box, text=item_def)

        def_displayed.append({"word": item_word, "type": item_type, "definition": item_def, "sentence": item_sentence})
    else:
        root.after_cancel(wait)
        clean_screen()
        root.after(2000)
        canvas.itemconfig(canvas_bg, image=game_over)

    show_answer()


def check_answer():
    global num_words
    root.after_cancel(wait)
    checked_words.append(item_word)
    num_words = len(checked_words)
    count_check.delete('1.0', END)
    count_check.insert('end', f"{num_words}")
    clean_screen()
    random_def()


def wrong_answer():
    global num_x
    root.after_cancel(wait)
    words_study.append({"word": item_word, "type": item_type, "definition": item_def, "sentence": item_sentence})
    num_x = len(words_study)
    count_x.delete('1.0', END)
    count_x.insert('end', f"{num_x}")
    unknown_data = pd.DataFrame(words_study)
    try:
        unknown_csv = pd.read_csv('Data/words_to_check.csv')
        unknown_dict = unknown_csv.to_dict()
    except FileNotFoundError:
        # Create a file
        unknown_data.to_csv('Data/words_to_check.csv', mode='w')
    else:
        if item_word not in unknown_dict["word"]:
            # Append data
            unknown_data.to_csv('Data/words_to_check.csv', mode='a', index=False, header=False)
        else:
            pass
    clean_screen()
    random_def()


# TODO Display answer
def show_answer():
    # word_key = list(item_def.keys())[list(item_def.values()).index(item_def)]
    wait_for_it()
    canvas.itemconfig(type_word, text=item_type)
    wait_for_it()
    canvas.itemconfig(sentence_word, text=f"'{item_sentence}'")
    wait_for_it()
    canvas.itemconfig(correct_answer, text=item_word.capitalize())


def wait_for_it():
    global wait, wait2
    var = IntVar()
    wait = root.after(3000, var.set, 1)
    print("waiting...")
    root.wait_variable(var)


def clean_screen():
    canvas.itemconfig(correct_answer, text="")
    canvas.itemconfig(type_word, text="")
    canvas.itemconfig(def_box, text="")
    canvas.itemconfig(sentence_word, text="")


# TODO Save in file fav words
def save_fav():
    fav_words.append({"word": item_word, "type": item_type, "definition": item_def, "sentence": item_sentence})
    fav_data = pd.DataFrame(fav_words)
    try:
        fav_csv = pd.read_csv('Data/favorite_words.csv')
    except FileNotFoundError:
        # Create a file
        fav_data.to_csv('Data/favorite_words.csv', mode='w')
    else:
        if item_word not in fav_csv:
            # Append data
            fav_data.to_csv('Data/favorite_words.csv', mode='a', index=False, header=False)
        else:
            pass


# TODO Create a reverse button

def reverse():
    last_def = def_displayed[-2]
    clean_screen()
    canvas.itemconfig(def_box, text=last_def["definition"])
    canvas.itemconfig(correct_answer, text=last_def["word"].capitalize())
    canvas.itemconfig(type_word, text=last_def["type"])
    canvas.itemconfig(sentence_word, text=f"'{last_def['sentence']}'")


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
canvas_bg = canvas.create_image(0, 0, image=bg, anchor="nw")

# TODO Display meaning in screen
correct_answer = canvas.create_text(74, 120, anchor="nw", width=244, fill="#FF3D74", text="", font='"Klee One" 18 bold')
type_word = canvas.create_text(74, 153, anchor="nw", width=244, fill="#07B31C", text="", font='"Klee One" 12 italic')
def_box = canvas.create_text(74, 181, anchor="nw", width=236, fill="#FF3D74", text="", font='"Klee One" 12 bold',
                             justify=LEFT)
sentence_word = canvas.create_text(74, 274, anchor="nw", width=238, fill="#07B31C", text="",
                                   font='"Klee One" 11 italic', justify=LEFT)
count_x = Text(root, borderwidth=0, height=1, width=2, fg="#DBDBDB", wrap=WORD, font='Helvetica 13 bold')
count_x.place(x=266, y=383)
count_check = Text(root, borderwidth=0, fg="#DBDBDB", height=1, width=2, wrap=WORD, font='Helvetica 13 bold')
count_check.place(x=326, y=382)

# TODO Create fav, correct, wrong and reverse buttons.
# Buttons img
start_img = PhotoImage(file="Images/start_button.png")
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
start_button = Button(root, image=start_img, borderwidth=0, height=113, width=248, command=random_def, relief="flat")
canvas.create_window(54, 168, anchor="nw", window=start_button)
Button(root, image=x_img, height=44, width=44, borderwidth=0, command=wrong_answer).place(x=114, y=502)
Button(root, image=check_img, height=44, width=45, borderwidth=0, command=check_answer).place(x=203, y=503)
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
