# TIP CALCULATOR
# If the bill $150.00, split between 5 people, with 12% tip. Round the result to 2 decimal places.
# Equation = (bill / person) * tip

# welcome message
print("Welcome to the tip calculator!!")

# takeing user input value
bill = float(input("What was the total bill? \n $"))

# Tip percentage message
tip = int(
    input("What percentage tip would you like to give? [10,12 or 15 %] \n %"))

# how many people
people = int(input("How many people to split the bill? \n"))

# tip calculation
tip_as_percentage = tip / 100
total_tip_amount = bill * tip_as_percentage
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people

final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")
