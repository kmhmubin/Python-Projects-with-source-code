# rock, paper and scissors games

import random

# ASCII Arts for rock, paper and scissors

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

# Game images
game_images = [rock, paper, scissors]

# entering user choice
user_choice = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper, 2 for scissor. \n => "))

# print game image by user choice
print(game_images[user_choice])

# random computer choice
computer_chocie = random.randint(0, 2)

# print game image by computer choice
print(game_images[computer_chocie])

# print(f"Computer chose {computer_chocie}")

"""
rock paper and scissor rules:

1. Rock wins against scissors.
2. Scissors win against paper.
3. Paper wins against rock. 
"""

# rules in logic
if user_choice == 0 and computer_chocie == 2:
    print("You win! 🎉")
elif user_choice == 0 and computer_chocie == 2:
    print("You lose.  ☠")
elif computer_chocie > user_choice:
    print("You lose. ☠")
elif user_choice > computer_chocie:
    print("You win!🎉 ")
elif computer_chocie == user_choice:
    print("It's a draw.")
elif user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, You Lose.  ☠")
