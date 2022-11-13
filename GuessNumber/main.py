import pyautogui
import random
from art import logo

game_on = True

EASY_LEVEL = 10
HARD_LEVEL = 5


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':\n")
    if difficulty == "easy":
        return EASY_LEVEL
    elif difficulty == "hard":
        return HARD_LEVEL
    else:
        print("Wrong Answer. Try again")
        # clear Pycharm console. More info below
        pyautogui.click(x=92, y=925)
        return game()


def shuffle():
    """Give a random number between 1 and 100"""
    number = random.randint(1, 100)
    return number


def check_guess(number, turns):
    while turns >= 1:
        print(f"You have {turns} attempts remaining to guess the number.")
        turns -= 1
        guess = int(input("Make a guess: "))
        if guess < number:
            print("Too Low.")
        elif guess > number:
            print("Too high.")
        else:
            print(f"You got it! The answer was {number}.")
            game_on = False
            return game_on
    print(f"You've run out of guesses, you lose.\n The number was {number}.")
    game_on = False
    return game_on


while game_on:
    number = shuffle()
    turns = game()
    check_guess(number, turns)
    try_again = input("Do you want to try again? Type 'yes' or 'no': ")
    if try_again == "no":
        print("Have a nice day.")
        game_on = False
    else:
        pyautogui.click(x=92, y=925)


# clear Pycharm console:
"""import pyautogui
from time import sleep
 sleep(5)  # hover your mouse over bin in this time
    mousepos = pyautogui.position()  # gets current pos of mouse
    x, y = mousepos  # storing mouse position
    print(mousepos)  # prints current pos of mouse
    sleep(5)  # get de pos (x,y)
    # then to clear it;
    pyautogui.click(x, y)  # and just put this line of code wherever you want to clear it"""