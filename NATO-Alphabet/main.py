import pandas as pd

# TODO 1. Create a dictionary in this format:
nato_data = pd.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

input_ok = False
while not input_ok:
    input_word = input("Write the word you want to transform in NATO: \n").upper()
    try:
        word_nato = [nato_dict[letter] for letter in input_word]
        print(f"\nYour NATO is: {word_nato}")
        input_ok = True
    except KeyError:
        print("Please, type only letters include in the alphabet.")




