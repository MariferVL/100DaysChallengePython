from random import choice, sample
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Style
import json


# TODO Change meaning
def random_def():
    pass


# TODO If answer is correct save in file to count them   if

# TODO If answer is wrong save in file to show them at the end   else

# TODO Show the asnwer
# answer = Button()


def check_answer():
    print("SECA")


def wrong_answer():
    print("Guardado para estudiar!")


# TODO Save in file fav words
def save_fav():
    print("GUARDADO")


# TODO Create a reverse button

def reverse():
    print("PA ATRAH!")


# TODO Display answer


### UI Setup ###

# create GUI Main window
root = Tk()

# Adjust size:
root.geometry("363x600")

# Add image file
bg = PhotoImage(file="Images/flash_card.png")

# create canvas to set flash card
canvas = Canvas(root, width=363, height=600)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg, anchor="nw")

# TODO Display meaning in screen

# TODO Create fav, correct, wrong and reverse buttons.
# Buttons img
canvas.create_text(178, 230, text="Def")
x_img = PhotoImage(file="Images/x_btn.png")
x_img = x_img.zoom(11)
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
x_button = Button(root, image=x_img, height=44, width=44, borderwidth=0, command=wrong_answer)
x_button.place(x=114, y=502)
check_button = Button(root, image=check_img, height=44, width=44, borderwidth=0, command=check_answer)
check_button.place(x=203, y=503)
fav_button = Button(root, image=fav_img, height=29, width=29, borderwidth=0, command=save_fav)
fav_button.place(x=282, y=493)
reverse_button = Button(root, image=reverse_img, height=29, borderwidth=0, width=29, command=reverse)
reverse_button.place(x=52, y=493)









# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')


# # Track Mouse Position:
# def motion(event):
#     x, y = event.x, event.y
#     print('{}, {}'.format(x, y))
#
#
# root.bind('<Motion>', motion)

# start the GUI
root.mainloop()
