from tkinter import *


# --------------------- GET QUOTES -------------------------- #

def get_quote():
    pass


# --------------------- UI SETUP ----------------------------- #

# creating window object
window = Tk()
# Window title
window.title("Kanye Says ..")
# add padding to window
window.config(padx=50, pady=50)

# creating a canvas
canvas = Canvas(width=300, height=414)
# add background image in a variable
background_image = PhotoImage(file="background.png")
# adding photos in a canvas
canvas.create_image(150, 207, image=background_image)
# quote text in the canvas
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"),
                                fill="white")
# canvas grid
canvas.grid(row=0, column=0)

# kanye image button
kanye_image = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_image, highlightthickness=0, border=0,command=get_quote)
kanye_button.grid(row=1, column=0)

# window running
window.mainloop()
