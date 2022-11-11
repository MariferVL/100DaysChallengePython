# Auction:

import pyautogui

bids = {}
actionActive = True


def auction():
    bids[name] = bid
    print(f"{name}, your bid of ${bid} has been approved. Good Luck!")


def winner(au_dict, maxvalue):
    for k, v in au_dict.items():
        if maxvalue == v:
            return k
    return "key doesn't exist"


def restart(au_dict):
    restart_in = input("Are there any other bidders?\n Type 'yes' or 'no'.\n").lower()
    if restart_in == "no":
        #   clear pycharm console. More info below
        pyautogui.click(x=92, y=776)
        maxvalue = max(au_dict.values())
        key = winner(bids, maxvalue)
        print(f"The highest bidder was {key}. Congrats!")
        print("Have a nice day!")
        return False
    elif restart_in == "yes":
        pyautogui.click(x=93, y=923)
        return True


while actionActive:
    print("Welcome to the secret auction program")
    name = input("What is your name?:\n").capitalize()
    bid = int(input(f"{name}, what is your bid?:\n $"))
    auction()
    actionActive = restart(bids)

# clear Pycharm console
"""import pyautogui

# to find the coordinates of the bin...
from time import sleep
sleep(2) # hover your mouse over bin in this time
mousepos = pyautogui.position() gets current pos of mouse
x,y = mousepos # storing mouse position 
print(mousepos) # prints current pos of mouse

# then to clear it;
pyautogui.click(x, y) # and just put this line of code wherever you want to clear it
"""

