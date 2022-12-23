from tkinter import *


class TriviaUI:
    def __init__(self, trivia):
        # create GUI Main window
        self.window = Tk()
        self.window.title("Who knows, knows.")
        #  self.window.wm_attributes('-transparentcolor', '#ab23ff')
        self.window.geometry("363x600")
        self.window.maxsize(363, 600)

        # UI Images
        bg = PhotoImage(file="images/flash_card1.png")
        self.game_over_img = PhotoImage(file="images/flash_card2.png")
        # Buttons img
        start_img = PhotoImage(file="images/start_button.png")
        x_img = PhotoImage(file="images/x_btn.png")
        x_img = x_img.zoom(13)
        x_img = x_img.subsample(33)
        check_img = PhotoImage(file="images/like_btn.png")
        check_img = check_img.zoom(11)
        check_img = check_img.subsample(33)

        # UI Canvas
        self.canvas = Canvas(width=363, height=100)
        self.canvas.pack(fill="both", expand=True)
        self.canvas_bg = self.canvas.create_image(0, 0, image=bg, anchor="nw")

        # Display question and score on screen
        self.text_box = self.canvas.create_text(74, 181, anchor="nw", width=236, fill="#FF3D74", text="",
                                                font='"Klee One" 12 bold', justify=LEFT)
        self.count_check = Text(borderwidth=0, height=1, width=2, fg="#DBDBDB", wrap=WORD, font='Helvetica 13 bold')
        self.count_check.place(x=326, y=386)

        self.count_x = Text(borderwidth=0, fg="#DBDBDB", height=1, width=2, wrap=WORD, font='Helvetica 13 bold')
        self.count_x.place(x=266, y=386)

        # Buttons UI
        self.start_button = Button(image=start_img, borderwidth=0, height=113, width=248, command=self.start_game,
                                   relief="flat")
        self.canvas.create_window(54, 168, anchor="nw", window=self.start_button)
        Button(image=x_img, height=44, width=44, borderwidth=0, command=self.press_false).place(x=114, y=502)
        Button(image=check_img, height=44, width=45, borderwidth=0, command=self.press_true).place(x=203, y=503)

        self.quiz = trivia

        # # Track Mouse Position:
        # def motion(event):
        #     x, y = event.x, event.y
        #     print('{}, {}'.format(x, y))
        #
        #  self.window.bind('<Motion>', motion)

        # start the GUI
        self.window.mainloop()

    def start_game(self):
        self.start_button.destroy()
        self.clean_screen()
        if self.quiz.still_has_questions():
            i_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text_box, text=i_text)
        else:
            self.game_over()

    def game_over(self):
        self.clean_screen()
        self.canvas.itemconfig(self.canvas_bg, image=self.game_over_img)

    def press_false(self):
        self.quiz.check_answer("false")
        self.update_score()
        self.start_game()

    def press_true(self):
        self.quiz.check_answer("true")
        self.update_score()
        self.start_game()

    def update_score(self):
        self.count_check.delete('1.0', END)
        self.count_check.insert('end', f"{self.quiz.score}")
        self.count_x.delete('1.0', END)
        self.count_x.insert('end', f"{self.quiz.wrong}")

    def clean_screen(self):
        self.canvas.itemconfig(self.text_box, text="")
