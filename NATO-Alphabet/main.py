import pandas as pd

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

student_data_frame = pd.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
nato_data = pd.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}

"""for (letter, word) in nato_data.iterrows():
    nato_dict[word.letter] = word.code
print(nato_dict)"""

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




