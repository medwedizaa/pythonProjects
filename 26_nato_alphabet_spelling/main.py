import pandas as pd


def get_spelled_word():
    name = input("Enter a word to be spelled: ")
    try:
        return [alphabet_dict[x.capitalize()] for x in name]
    except KeyError:
        print("Sorry, only letters in th alphabet please")
        return get_spelled_word()


df = pd.read_csv('nato_phonetic_alphabet.csv')
alphabet_dict = {row['letter']: row['code'] for (index, row) in df.iterrows()}

result = get_spelled_word()
print(result)
