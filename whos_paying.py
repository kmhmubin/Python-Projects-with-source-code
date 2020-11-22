import random

# creating a random seed nubmer
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
nameAsCSV = input("Give me everybody's name, seperated by commas.\n =>")
names = nameAsCSV.split(", ")

# Get the total number of items in list
num_items = len(names)

# Generate random numbers between 0 and the last item on the list
random_choice = random.randint(0, num_items - 1)
preson_who_will_pay = names[random_choice]
print(preson_who_will_pay + " is going to buy the meal today!")
