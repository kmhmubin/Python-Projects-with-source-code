# Your life in weeks
# A program that tells us how many days, weeks, months we have left if we live until 90 days

# takeing user input
age = input("What is your current age?")

# convert input string to int value
age_in_int = int(age)

# Calculation for years,months,weeks and days
years_remaining = 90 - age_in_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

# Printing the result

message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left"

print(message)
