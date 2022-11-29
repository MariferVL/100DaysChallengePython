from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#E14D2A"
GREEN = "#379237"
YELLOW = "#f7f5dd"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check = ""
timer_on = None

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def start_timer():
    concentration()


def end_timer():
    global timer_on
    reset_timer()
    window.after_cancel(timer_on)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro Timer")
window.config(width=333, height=333, padx=110, pady=55, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer = canvas.create_text(100, 133, text="00:00", font=("lucida", 33, "bold"), fill=YELLOW)
canvas.grid(column=1, row=1)

title = Label(text="   Timer  ", padx=11, pady=11, bg=YELLOW, fg=GREEN, font=("Century Gothic", 33, "bold"))
title.grid(column=1, row=0)

start_btn = Button(text="Start", bg=RED, fg=YELLOW, padx=8, pady=8, relief="flat",
                   font=("Comic Sans MS", 11, "bold"), command=start_timer)
start_btn.grid(column=0, row=3)

reset_btn = Button(text="Reset", bg=RED, fg=YELLOW, padx=8, pady=8, relief="flat",
                   font=("Comic Sans MS", 11, "bold"), command=end_timer)
reset_btn.grid(column=2, row=3)

times_past = Label(text=check, padx=11, pady=11, bg=YELLOW, fg=GREEN, font="lucid 22 bold")
times_past.grid(column=1, row=2)


def concentration():
    global reps
    global check
    working = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    reps += 1
    if reps % 8 == 0:
        check += "🍅"
        times_past.config(text=check)
        check = ""
        count_down_sec(long_break)
        title.config(text="Break", font=("Century Gothic", 33, "bold"), fg=RED)

    elif reps % 2 == 0:
        check += "🍅"
        times_past.config(text=check)
        count_down_sec(short_break)
        title.config(text="Break", font=("Century Gothic", 33, "bold"), fg="#FFE15D")
    else:
        times_past.config(text=check)
        count_down_sec(working)
        title.config(text="Work", font=("Century Gothic", 33, "bold"), fg=GREEN)


def count_down_sec(seconds):
    global timer_on
    minutes = math.floor(seconds/60)
    sec_left = seconds % 60
    if sec_left < 10:
        sec_left = "0" + str(sec_left)
    canvas.itemconfig(timer, text=f"{minutes}:{sec_left}")
    if seconds > 0:
        timer_on = window.after(1000, count_down_sec, seconds-1)
    else:
        concentration()


def reset_timer():
    global check
    global reps
    check = ""
    reps = 0
    times_past.config(text=check)
    canvas.itemconfig(timer, text="00:00")
    title.config(text="   Timer  ")

window.mainloop()
