from random import randint

EASY_LEVEL_TURNS = 15
HARD_LEVEL_TURNS = 10


def checking_answer(guess, answer, turns):
    if guess > answer:
        print("Too high.")
        # global turns
        # turns -= 1
        return turns - 1
    elif guess < answer:
        print("Too low.")
        # turns -= 1
        return turns - 1
    else:
        print(f"you got it! The answer was{answer}.")


def set_difficulty():
    level_game = input("Choose a difficultly: Type 'easy' or 'hard': ")
    if level_game == 'hard':
        return HARD_LEVEL_TURNS

    else:
        return EASY_LEVEL_TURNS


def game():
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 200.")

    answer = randint(1, 200)
    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"you have {turns} attempts remaining to guess the number.")
        guess = int(input("Enter a number"))
        turns = checking_answer(guess, answer, turns)
        if turns == 0:
            print("You lose")
            return
        elif guess != answer:
            print("guess again.")


game()
