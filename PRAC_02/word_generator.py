import random

VOWELS = "aeiou"
CONSONENTS = "bcdfghjklmnpqrstvwxyz"



def main():
    word_format = input("Input word format (c or v)").lower()
    word = ""

    while not Is_Valid_Input(word_format):
        print("invalid word format")
        word_format = input("> ")

    for kind in word_format:
        if kind == "c":
            word += random.choice(CONSONENTS)
        else:
            word += random.choice(VOWELS)
    print(word)

def Is_Valid_Input(word_format):

    if word_format.isnumeric():
        return False

    return True

main ()