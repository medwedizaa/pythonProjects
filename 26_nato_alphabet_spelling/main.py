import pandas as pd

df = pd.read_csv('nato_phonetic_alphabet.csv')
alphabet_dict = {row['letter']: row['code'] for (index, row) in df.iterrows()}

name = input("Enter a name to be spelled: ")
result = [alphabet_dict[x.capitalize()] for x in name]
print(result)
