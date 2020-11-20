# BMI calculator

# Taking user input for height
height = input("Enter you height in m: ")
weight = input("Enter your wight in kg: ")

# converting strings to number

weight_as_int = int(weight)
height_as_float = float(height)

# calculate the bmi value
bmi = weight_as_int / (height_as_float ** 2)

# print(int(bmi))
print(f"Your BMI Value is: {int(bmi)}")
