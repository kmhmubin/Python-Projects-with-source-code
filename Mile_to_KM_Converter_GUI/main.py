from tkinter import *

# creating window object
window = Tk()
# Program title
window.title("Miles to Kilometer Converter")

# adding padding to window
window.config(padx=20, pady=20)

# taking user input
miles_input = Entry(width=7)
# grid placement
miles_input.grid(column=2, row=0)
# showing input label
miles_label = Label(text="Miles: ")
# grid placement
miles_label.grid(column=1, row=0)
# another text label
is_equal_label = Label(text="Equal to")
# grid placement
is_equal_label.grid(column=2, row=1)
# kilometer result label, default 0
kilometer_result_label = Label(text="0")
# grid placement
kilometer_result_label.grid(column=2, row=2)
# showing result label
kilometer_label = Label(text="KM:")
# grid placement
kilometer_label.grid(column=1, row=2)


# mile to km calculation
def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    kilometer_result_label.config(text=f"{km}")


# calculator button
calculate_button = Button(text="Calculate", command=miles_to_km)
# button placement
calculate_button.grid(column=2, row=3)

# continue run the window object
window.mainloop()
