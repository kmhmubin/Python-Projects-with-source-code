# PASSWORD GENERATOR
from tkinter import *

# ------ CONSTANT ---- #
GREENISH_YELLOW = "#E6EDB7"
GREENISH_WHITE = "#FDFCEF"
LIGHT_SKY = "#C0E5E4"
COURIER_FONT = "Courier"

# ------------------- PASSWORD GENERATOR ----------------------------- #


# ------------------- SAVED PASSWORD ----------------------------- #


# ------------------- UI SETUP ----------------------------- #

# creating window object
window = Tk()

# window title
window.title("Password Generator")

# add custom favicon
window.iconbitmap(r'favicon.ico')

# add padding and background color
window.config(padx=20, pady=20, bg=GREENISH_WHITE)

# canvas size
canvas = Canvas(height=300, width=300, bg=GREENISH_WHITE, highlightthickness=0)

# assign the image location to a variable
logo_image = PhotoImage(file="security.png")
# add image in the canvas in the center by "/" half of the dimension
canvas.create_image(150, 150, image=logo_image)
canvas.pack()

# window run
window.mainloop()
