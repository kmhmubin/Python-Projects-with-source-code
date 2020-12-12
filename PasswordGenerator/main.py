# PASSWORD GENERATOR
import pyperclip
from tkinter import *
from random import choice, randint, shuffle

from tkinter import messagebox

# ------ CONSTANT ---- #

GREENISH_YELLOW = "#E6EDB7"
GREENISH_WHITE = "#FDFCEF"
LIGHT_SKY = "#C0E5E4"
LIGHT_GREEN = "#92E3A9"
COURIER_FONT = "Courier"


# ------------------- PASSWORD GENERATOR ----------------------------- #

def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    # add all password in a list
    password_list = password_letters + password_symbols + password_numbers
    # shuffle those generated password in the list
    shuffle(password_list)

    # join password
    password = "".join(password_list)
    # show generated password in the password label field
    password_entry.insert(0, password)
    # copy password on the clipboard automatically
    pyperclip.copy(password)


# ------------------- SAVED PASSWORD ----------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    # checking empty fields
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Opps", message=" Please fill up the empty fields.")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"Is It Correct Info \n Email: {email} " f"\n Password: {password} \nIs "
                                               f"it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password} \n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ------------------- UI SETUP ----------------------------- #

# creating window object
window = Tk()

# window title
window.title("Password Generator")

# add custom favicon
window.iconbitmap(r'favicon.ico')

# add padding and background color
window.config(padx=60, pady=60, bg=GREENISH_WHITE)

# canvas size
canvas = Canvas(height=300, width=300, bg=GREENISH_WHITE, highlightthickness=0)

# assign the image location to a variable
logo_image = PhotoImage(file="security.png")
# add image in the canvas in the center by "/" half of the dimension
canvas.create_image(150, 150, image=logo_image)
# assign the grid for the canvas
canvas.grid(row=0, column=1)

# TODO: Labels

# website labels
website_label = Label(text="Website:", bg=GREENISH_WHITE, font=COURIER_FONT)
# website label on grid
website_label.grid(row=1, column=0)
# email labels
email_label = Label(text="Email:", bg=GREENISH_WHITE, font=COURIER_FONT)
# email label on grid
email_label.grid(row=2, column=0)
# password labels
password_label = Label(text="Password:", bg=GREENISH_WHITE, font=COURIER_FONT)
# password label on grid
password_label.grid(row=3, column=0)

# TODO: Labels entry
# website entry
website_entry = Entry(width=55, font=COURIER_FONT)
# website entry placement
website_entry.grid(row=1, column=1, columnspan=2)
# focus the website entry
website_entry.focus()
# email entry
email_entry = Entry(width=55, font=COURIER_FONT)
# email entry placement on grid
email_entry.grid(row=2, column=1, columnspan=2, padx=10, pady=10)
# pre populated value
email_entry.insert(0, "example@example.com")
# password entry
password_entry = Entry(width=43, font=COURIER_FONT)
# password entry placement on grid
password_entry.grid(row=3, column=1)

# TODO: Buttons

# generate password button
generate_password_button = Button(text="Generate", font=COURIER_FONT, bg=LIGHT_SKY, command=password_generator)
# generate button placement on grid
generate_password_button.grid(row=3, column=2)

# add password on file button
save_button = Button(text="Save", width=55, bg=GREENISH_YELLOW, font=COURIER_FONT, command=save)
# save button placement on the grid
save_button.grid(row=4, column=1, columnspan=2, padx=10, pady=10)
# window run
window.mainloop()
