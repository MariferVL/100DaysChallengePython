from random import sample
from extras import logo, data
import pyautogui
from time import sleep


picked_list = []
game_on = True


def pick():
    picked_list = sample(range(0, 50), 2)
    return picked_list


def display():
    sleep(1)
    options = pick()
    dict1 = data[options[0]]
    dict2 = data[options[1]]
    if "name" and "description" and "country" in dict1.keys():
        print("Compare: ")
        print(f"  A: {dict1['name']}, a {dict1['description']}, from {dict1['country']}.")
    print("       v/s")
    if "name" and "description" and "country" in dict2.keys():
        print(f"  B: {dict2['name']}, a {dict2['description']}, from {dict2['country']}.")
    return dict1['follower_count'], dict2['follower_count']


followers = []


def check():
    """Choose 2 people randomly from a dict."""
    next_round = True
    score = 0
    while next_round:
        followers = display()
        guess = input("\nWho has more followers? Type 'A' or 'B': ").capitalize()
        if guess == "A" and followers[0] > followers[1]:
            score += 1
            print(f"\nYou're right! Current score: {score}\n")
        elif guess == "B" and followers[0] < followers[1]:
            score += 1
            print(f"\nYou're right! Current score: {score}\n")
        else:
            print(f"\nSorry, that's wrong. Final score: {score}\n")
            next_round = False
            return next_round


def again():
    try_again = input("\nDo you want to try again? Type 'yes' or 'no': ").lower()
    if try_again == "yes":
        pyautogui.click(x=92, y=925)
        return True
    elif try_again == "no":
        print("Have a nice day!")
        return False
    else:
        print("Wrong answer.")
        return False


while game_on:
    print(logo)
    check()
    game_on = again()


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
