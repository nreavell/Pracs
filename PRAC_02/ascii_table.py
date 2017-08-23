# Editable properties

MIN_ASCII = 33
MAX_ASCII = 127

def main():

    YOUR_CHARACTER = input("Enter a character: ")

    while not Is_Valid_Character(YOUR_CHARACTER):
        print("Invalid value")
        YOUR_CHARACTER = input("> ")

    ASCII_NUMBER_OUTPUT = ord(YOUR_CHARACTER)
    print("The ASCII code for {}  is {}".format(YOUR_CHARACTER, ASCII_NUMBER_OUTPUT))

    YOUR_NUMBER = (input(("Enter a number between {} and {}: ".format(MIN_ASCII,MAX_ASCII))))

    while not Is_Valid_Number(YOUR_NUMBER):
        print("Invalid value")
        YOUR_NUMBER = input("> ")

    ASCII_CHARACTER_OUTPUT = chr(int(YOUR_NUMBER))
    print("The character for {} is {}".format(YOUR_NUMBER, ASCII_CHARACTER_OUTPUT))

    print("{} \n{}\n...\n{}\n{}".format())

def Is_Valid_Number(YOUR_NUMBER):

    if YOUR_NUMBER.isdigit():
        if MIN_ASCII <= int(YOUR_NUMBER) <= MAX_ASCII:
            return True

    return False

def Is_Valid_Character(YOUR_CHARACTER):

    if YOUR_CHARACTER.isdigit() == False:
        return True

    return False

main()