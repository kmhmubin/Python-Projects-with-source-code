from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
# creating window
window = Tk()
# window title
window.title("Pomodoro")
# add padding to the window and add background color
window.config(padx=100, pady=50, bg=YELLOW)
# creating a canvas, add background color and remove border around image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# assign the image location to a variable
tomato_img = PhotoImage(file="tomato.png")
# add image in the canvas in the center by "/" half of the dimension
canvas.create_image(100, 112, image=tomato_img)
# add text on the top of tomato photo and customize text values
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# show the canvas on the window
canvas.pack()

# window show up
window.mainloop()
