from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
DEEP_GREEN = "#16a596"
WHITE = "#fbf6f0"
YELLOW = "#f7f5dd"
ORANGE = "#ec524b"
FONT_NAME = "Courier"
BUTTON_FONT = "Consolas"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    # after hit the reset button it become 0
    window.after_cancel(timer)
    # text time 00:00
    canvas.itemconfig(timer_text, text="00:00")
    # title label "Timer"
    title_label.config(text="Timer")
    # reset check marks
    check_mark.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    # convert number into minutes
    work_seconds = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    # checking reps
    if reps % 8 == 0:
        count_down(long_break)
        # change the text label
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break)
        # change the text label
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_seconds)
        # change the text label
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    # covert counter into time
    count_minute = math.floor(count / 60)
    count_seconds = count % 60
    # replace 0 to 00
    if count_seconds == 10:
        count_seconds == f"0{count_seconds}"
    # replace the canvas timer text
    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
# creating window
window = Tk()
# window title
window.title("Pomodoro")
# add padding to the window and add background color
window.config(padx=100, pady=50, bg=YELLOW)
# changing default program icon to tomato icon
window.iconbitmap(r'favicon.ico')

# title label, add text foreground, add background and font values
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
title_label.grid(column=1, row=0)

# TODO: Creating a canvas
# creating a canvas, add background color and remove border around image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# assign the image location to a variable
tomato_img = PhotoImage(file="tomato.png")
# add image in the canvas in the center by "/" half of the dimension
canvas.create_image(100, 112, image=tomato_img)
# add text on the top of tomato photo and customize text values
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# show the canvas on the window
canvas.grid(column=1, row=1)

# TODO: Creating Buttons
# start button, remove border, add custom style and font and command key
start_button = Button(text="Start", bg=DEEP_GREEN, fg=WHITE, highlightthickness=0, font=(BUTTON_FONT, 15, "bold"),
                      command=start_timer)
# start button position
start_button.grid(column=0, row=2)
# reset button
reset_button = Button(text="Reset", bg=ORANGE, fg=WHITE, highlightthickness=0, font=(BUTTON_FONT, 15, "bold"),
                      command=reset_timer)
reset_button.grid(column=2, row=2)

# TODO: Checkmark Show
# show checkmark icons
check_mark = Label(fg=GREEN, bg=YELLOW, font=10)
# position of the checkmark icons
check_mark.grid(column=1, row=3)

# window show up
window.mainloop()
