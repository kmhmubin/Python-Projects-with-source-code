import random

# word list


chosen_word = random.choice(word_list)

guess = input("Guess a letter: ").lower()

for letter in chosen_word:
    if letter == guess:
        print("Rigth")
    else:
        print("Wrong")
