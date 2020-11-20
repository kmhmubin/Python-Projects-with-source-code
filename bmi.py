# BMI calculator
# Instructions
# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

# It should tell them the interpretation of their BMI based on the BMI value.

# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

# Solution

# Taking user input for height
height = float(input("Enter you height in m: "))
weight = float(input("Enter your wight in kg: "))


# calculate the bmi value
bmi = round(weight / height ** 2)

# Checking the condition for BMI Value
if bmi < 18.5:
    print(f"Your BMI {bmi}, you are underweight")
elif bmi < 25:
    print(f"Your BMI {bmi}, you are normal weight")
elif bmi < 30:
    print(f"Your BMI {bmi}, You are slightly overweight")
elif bmi < 35:
    print(f"Your BMI {bmi}, You are obese")
else:
    print(f"Your BMI {bmi}, You are clinically obese")


