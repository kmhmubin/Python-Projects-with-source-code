# rock, paper and scissors games

# import random package
import random

# ASCII Arts for rock, paper and scissors
# Adding ASCII art into a variable

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Adding Game Images into a list
game_images = [rock, paper, scissors]

# Taking input from user choice
user_choice = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper, 2 for scissor. \n => "))

print("User Choice: ")    

# print game image by user choice
print(game_images[user_choice])

# random computer choice
computer_chocie = random.randint(0, 2)

print("Computer Choice: ")

# print game image by computer choice
print(game_images[computer_chocie])

# rules in logic
if user_choice == 0 and computer_chocie == 2:
    print("You win! 🎉")
elif computer_choice == 0 and user_chocie == 2:
    print("You lose.  ☠")
elif computer_chocie > user_choice:
    print("You lose. ☠")
elif user_choice > computer_chocie:
    print("You win!🎉 ")
elif computer_chocie == user_choice:
    print("It's a draw.")
elif user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, You Lose.  ☠")
