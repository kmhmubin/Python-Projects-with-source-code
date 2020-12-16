from tkinter import *

# ------------- CONSTANT -------------------------- #
THEME_COLOR = "#9ba4b4"
SCORE_COLOR = "#14274e"
CANVAS_BG = "#f1f6f9"
BAHNSCHRIFT = "Bahnschrift"


# ------------------ Class --------------------- #

class QuizInterface:

    def __init__(self):
        # assign the tkinter class
        self.window = Tk()
        # window title
        self.window.title("Quizer App")
        # add padding to the window
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # add score label text
        self.score_label = Label(text="Score: 0", fg=SCORE_COLOR, bg=THEME_COLOR, font=BAHNSCHRIFT)
        # assign label on the window grid
        self.score_label.grid(row=0, column=1)

        # creating a canvas
        self.canvas = Canvas(width=300, height=250, bg=CANVAS_BG)
        # question text
        self.question_text = self.canvas.create_text(150, 125, text="Some Question text", fill=SCORE_COLOR,
                                                     font=(BAHNSCHRIFT, 20, "italic"))
        # canvas grid
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # true button
        true_image = PhotoImage(file="images/tick.png")
        self.true_button = Button(image=true_image, bg=THEME_COLOR, highlightthickness=0, borderwidth=0)
        self.true_button.grid(row=2, column=1)

        # false button
        false_image = PhotoImage(file="images/cross.png")
        self.false_button = Button(image=false_image, bg=THEME_COLOR, highlightthickness=0, borderwidth=0)
        self.false_button.grid(row=2, column=0)
        # run the program
        self.window.mainloop()
