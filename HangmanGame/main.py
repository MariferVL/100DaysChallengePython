import random
from extras import word_list, lista_palabras, stages

language = input("Do wou want to play in Spanish or English?\n Type S for Spanish and E for English\n").upper()
if language == "E":
    chosen_word = random.choice(word_list)
elif language == "S":
    chosen_word = random.choice(lista_palabras)
else:
    print("Write just 1 letter | Escribe solo una letra")
word_length = len(chosen_word)
lives = 6

lines = []
for char in range(word_length):
    lines += "_"
end_game = False
i = 6
print(stages[i])
while not end_game:
    display = " ".join(lines)
    print(display)
    guess = input("\n Guess a letter | Adivina una letra:\n").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            lines[position] = letter
    if guess not in chosen_word:
        lives -= 1
        i -= 1
        print(stages[i])
        if lives == 0:
            end_game = True
            print(f"The word was | La palabra era: {chosen_word}")
            print("You Lose. Try Again! | Perdiste. ¡Intenta Nuevamente!")
    elif "_" not in lines:
        end_game = True
        display = " ".join(lines)
        print(display)
        print("\n You Win! | ¡Ganaste!")
