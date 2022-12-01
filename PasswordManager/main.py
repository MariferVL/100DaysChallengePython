# Python program to generate random
# password using Tkinter module
from random import choice, sample
from tkinter import *
from tkinter.ttk import Combobox, Style
import json
import pyperclip
import emoji

# Logo colors
WHITE = "#ffffff"
RED = "#fc0000"
BLACK = "#00071b"


### Password Generator ###

def create_pass():
    """Function to create password"""
    pass_input.delete(0, END)

    # Get the length of password
    length = var1.get()

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789!@#$%^&*()"
    creating_pass = ""

    # if strength selected is low
    if var.get() == 1:
        creating_pass = ''.join([choice(lower) for i in range(0, length)])
        return creating_pass

    # if strength selected is medium
    elif var.get() == 0:
        left = length - 3
        creating_pass = ''.join([choice(lower) for i in range(0, length)])
        creating_pass = creating_pass + ''.join(choice(upper) for i in range(3))
        password = ''.join(sample(creating_pass, len(creating_pass)))
        return password

    # if strength selected is strong
    elif var.get() == 3:
        left = length - 6
        creating_pass = ''.join([choice(lower) for i in range(0, length)])
        creating_pass = creating_pass + ''.join(choice(upper) for i in range(3))
        creating_pass = creating_pass + ''.join(choice(digits) for i in range(3))
        password = ''.join(sample(creating_pass, len(creating_pass)))
        return password
    else:
        print("Please choose an option")


def generate():
    """Function to generate password"""
    final_password = create_pass()
    pass_input.insert(0, final_password)


def copy_pass():
    """Function to copy password to clipboard"""
    pass_created = pass_input.get()
    pyperclip.copy(pass_created)


# Change button hover color
def hover(e):
    e.widget['bg'] = RED
    e.widget['fg'] = BLACK


def on_click(e):
    e.widget['bg'] = RED
    e.widget['fg'] = BLACK
    e.widget['font'] = ("Century Gotic", 8, "bold")


def on_leave(e):
    e.widget['bg'] = BLACK
    e.widget['fg'] = RED
    e.widget['font'] = ("Century Gotic", 8, "bold")


### Save Password ###

def save_info():
    website = web_input.get()
    username = email_input.get()
    password = pass_input.get()
    data = {
        website: {
            "email": username,
            "password": password,
        }
    }
    try:
        with open("passlaxy.json", "r") as file:
            # Read the .json
            saved_file = json.load(file)
    except FileNotFoundError:
        with open("passlaxy.json", "w") as file:
            # Create the .json.
            json.dump(data, file, indent=4)
    else:
        saved_file.update(data)
        with open("passlaxy.json", "w") as file:
            # Save Updated data in .json.
            json.dump(saved_file, file, indent=4)
    finally:
        web_input.delete(0, 'end')
        pass_input.delete(0, 'end')
        print(file)

### UI Setup ###

# create GUI root
# Main window
window = Tk()
var = IntVar()
var1 = IntVar()

# Title of your GUI root
window.title("Passlaxy")
# Setting color and pad of main window
window.config(padx=88, pady=88, bg=WHITE)
# root.config(width=800, height=800, padx=20, pady=20, bg=WHITE)

# Creating style element
s1 = Style()
# First argument is the name of style. Needs to end with: .TRadiobutton
s1.configure('Black.TRadiobutton', bg=WHITE,
             fg=BLACK, font=("Century Gothic", 8, "bold"))

# create canvas that to set logo
canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
img = PhotoImage(file="passlaxyLogo1.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0, columnspan=5)

# create website label and entry to show
web_label = Label(text="Website:", bg=WHITE, fg=BLACK, font=("Century Gothic", 11, "bold"))
web_label.place(x=56, y=199)
web_input = Entry(width=44, bg=BLACK, fg=WHITE, font=("Century Gotic", 11, "bold"), insertbackground="white")
web_input.grid(column=2, row=1, columnspan=2)
locked = emoji.emojize(":locked_with_key:")

#TODO add emoji
web_input.insert(0, f"{locked}")
web_input.focus()

# create email label and entry to show
email_label = Label(text="Email/Username:", bg=WHITE, fg=BLACK, font=("Century Gotic", 11, "bold"), height=2)
email_label.grid(column=1, row=2)
email_input = Entry(width=44, bg=BLACK, fg=WHITE, font=("Century Gotic", 11, "bold"), insertbackground="white")
email_input.grid(column=2, row=2, columnspan=2)
email_input.insert(0, "@gmail.com")

# create label for password length
len_label = Label(text="Length:", bg=WHITE, fg=BLACK, font=("Century Gotic", 11, "bold"), height=2)
len_label.place(x=63, y=257)

space_btwn2: Label = Label(bg=WHITE, height=2)
space_btwn2.grid(column=2, row=3, columnspan=2)

# Combo Box for length of your password
combo = Combobox(textvariable=var1, width=3)
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16,
                   17, 18, 19, 20, 21, 22, 23, 24, 25,
                   26, 27, 28, 29, 30, 31, 32, "Length")
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.place(x=133, y=266)

# Radio Buttons for deciding the
# strength of password
# Default strength is Medium
radio_label = Label(text="Strength:", bg=WHITE, fg=BLACK, font=("Century Gotic", 11, "bold"))
radio_label.place(x=225, y=264)
radio_low = Radiobutton(text="Low", variable=var, value=1, highlightcolor=RED, activeforeground=RED,
                        activebackground=WHITE, bg=WHITE, fg=BLACK, selectcolor=WHITE,
                        font=("Century Gotic", 8, "bold"))
radio_low.place(x=298, y=264)
radio_middle = Radiobutton(text="Medium", variable=var, value=0, highlightcolor=RED, activeforeground=RED,
                           activebackground=WHITE, bg=WHITE, fg=BLACK, selectcolor=WHITE,
                           font=("Century Gotic", 8, "bold"))
radio_middle.place(x=349, y=264)
radio_strong = Radiobutton(text="Strong", variable=var, value=3, highlightcolor=RED, activeforeground=RED,
                           activebackground=WHITE, bg=WHITE, fg=BLACK, selectcolor=WHITE,
                           font=("Century Gotic", 8, "bold"))
radio_strong.place(x=419, y=264)

# create password label and entry to show
pass_label = Label(text="Password:", bg=WHITE, fg=BLACK, font=("Century Gotic", 11, "bold"), height=2)
pass_label.place(x=45, y=292)
pass_input = Entry(width=30, bg=RED, fg=WHITE, font=("Century Gotic", 11, "bold"))
pass_input.grid(column=2, row=4)

# create Buttons Generate
# which will generate the password
generate_btn = Button(text="Generate", width=13, bg=BLACK, fg=RED, font=("Century Gotic", 8, "bold"), command=generate)
generate_btn.grid(column=3, row=4)
generate_btn.bind("<ButtonPress>", on_click)
generate_btn.bind("<Enter>", hover)
generate_btn.bind("<Leave>", on_leave)

space_btwn = Label(bg=WHITE)
space_btwn.grid(column=2, row=7, columnspan=2)

# create Button Copy which will copy
# password to clipboard
copy_btn = Button(text="Copy", width=50, bg=BLACK, fg=RED, font=("Century Gotic", 8, "bold"), command=copy_pass)
copy_btn.grid(column=2, row=8, columnspan=2)
copy_btn.bind("<Button>", on_click)
copy_btn.bind("<Enter>", hover)
copy_btn.bind("<Leave>", on_leave)

# create Button Save to add info in file
save_btn = Button(text="Save", width=50, bg=BLACK, fg=RED, font=("Century Gotic", 8, "bold"), command=save_info)
save_btn.grid(column=2, row=9, columnspan=2)
save_btn.bind("<ButtonPress>", on_click)
save_btn.bind("<Enter>", hover)
save_btn.bind("<Leave>", on_leave)

# start the GUI
window.mainloop()
