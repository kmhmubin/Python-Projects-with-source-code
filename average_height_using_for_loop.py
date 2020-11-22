# Finding average height using for loop.

# takeing students height and sperated
student_heights = input(
    "Input a list of students heights. Seperated by commas.\n => ").split()

# checking the input in list
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# printing the students height list
print(f"Student Height List: {student_heights}")

# total sum of heigth using for loop
total_height = 0
for height in student_heights:
    total_height += height

print(f"Total height: {total_height}")

# Total length of students
number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(f"Total Number of Students: {number_of_students}")

# Average Height of students
average_height = round(total_height / number_of_students)

print(f"Average Height of Studens: {average_height}")
