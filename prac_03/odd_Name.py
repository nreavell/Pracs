# """Nathan Reavell"""

def main():

    step = int(input("How many steps? "))

    name = get_name()

    print_name(name, step)


def print_name(name, step):
    for char in range(1, len(name), step):
        print(name[char])


def get_name():
    name = input("What is your name? ")
    while not is_valid(name):
        print("Name is invalid")
        name = input(">>> ")
    return name


def is_valid(Name):
    if Name == "":
        return False

    return True

main()