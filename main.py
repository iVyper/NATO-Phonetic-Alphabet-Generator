"""
NATO Phonetic Alphabet Generator

This script reads a CSV of the NATO phonetic alphabet (letter → code word),
builds a lookup dictionary, prompts the user for a word, and outputs the
corresponding sequence of code words.
"""

import pandas as pd

# Load the CSV file into a DataFrame. Each row has 'letter' and 'code' columns.
data = pd.read_csv('./nato_phonetic_alphabet.csv')

# Build a dictionary mapping each uppercase letter to its NATO code word.
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}

# Prompt the user for a word and convert it to uppercase to match dictionary keys.
user_input = input("Enter a word: ").upper()

# Translate each letter in the input to its code word, if it exists in the dictionary.
# Non-alphabet characters are simply skipped.
phonetic_output = [phonetic_dict[letter] for letter in list(user_input) if letter in phonetic_dict]

# Display the list of NATO code words.
print(phonetic_output)