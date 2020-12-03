from random import randint

logo = """

 $$$$$$\                                                $$$$$$$$\ $$\                       $$\   $$\                         $$\
$$  __$$\                                               \__$$  __|$$ |                      $$$\  $$ |                        $$ |
$$ /  \__|$$\   $$\  $$$$$$\   $$$$$$$\  $$$$$$$\          $$ |   $$$$$$$\   $$$$$$\        $$$$\ $$ |$$\   $$\ $$$$$$\$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\
$$ |$$$$\ $$ |  $$ |$$  __$$\ $$  _____|$$  _____|         $$ |   $$  __$$\ $$  __$$\       $$ $$\$$ |$$ |  $$ |$$  _$$  _$$\ $$  __$$\ $$  __$$\ $$  __$$\
$$ |\_$$ |$$ |  $$ |$$$$$$$$ |\$$$$$$\  \$$$$$$\           $$ |   $$ |  $$ |$$$$$$$$ |      $$ \$$$$ |$$ |  $$ |$$ / $$ / $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|
$$ |  $$ |$$ |  $$ |$$   ____| \____$$\  \____$$\          $$ |   $$ |  $$ |$$   ____|      $$ |\$$$ |$$ |  $$ |$$ | $$ | $$ |$$ |  $$ |$$   ____|$$ |
\$$$$$$  |\$$$$$$  |\$$$$$$$\ $$$$$$$  |$$$$$$$  |         $$ |   $$ |  $$ |\$$$$$$$\       $$ | \$$ |\$$$$$$  |$$ | $$ | $$ |$$$$$$$  |\$$$$$$$\ $$ |
 \______/  \______/  \_______|\_______/ \_______/          \__|   \__|  \__| \_______|      \__|  \__| \______/ \__| \__| \__|\_______/  \_______|\__|


"""


# add game levels
EASY_lEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer, turns):
    """
    Check the user's guess against actual answer. If not right then minus 1 lives.
    """
    if guess > answer:
        print("Too High")
        return turns - 1
    elif guess < answer:
        print("Too Low")
        return turns - 1
    else:
        print(f" You got it! The answer was {answer} ")


def set_difficulty():
    """
    To set game difficulty
    """
    level = input("Choose a difficulty. Type 'easy' or 'hard'\n=> ")
    if level == "easy":
        return EASY_lEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    """
    main game function
    """
    print(logo)
    print("Welcome to the Number Guessing Game!!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer} ")

    turns = set_difficulty()
    # repeat the guessing if they get it wrong until 0 by difficulty
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number. ")

        # let the user guess the number
        guess = int(input("Make a guess: "))

        # Track the number of turns and reduce by 1 if they get it wrong
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess Again")
        else:
            print("Game Finish.")


# run the main game function
game()
