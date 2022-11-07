import random
from images import logo, rock, paper, scissors

print(logo)
answer = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
options = [rock, paper, scissors]
player1 = options[answer]
player2 = random.choice(options)

print(player1)
print(f"Computer chose: {player2}")

if player1 == rock and player2 == scissors:
    print("You Win!")
elif player1 == paper and player2 == rock:
    print("You Win!")
elif player1 == scissors and player2 == paper:
    print("You Win!")
elif player1 == player2:
    print("It's a Draw.")
else:
    print("You Lose :(")
