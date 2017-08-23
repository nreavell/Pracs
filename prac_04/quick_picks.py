import random

numbers_per_line = 6
smallest_number = 1
largest_number = 45
quick_picks = int(input("How many quick picks? "))

while quick_picks < 0:
    print("number is invalid")
    quick_picks = int(input("How many quick picks? "))

for row in range(0,quick_picks):
    for value in range(numbers_per_line):
        number = random.randint(smallest_number, largest_number)
        print("{:2}".format(number), end=' ')
    print()
