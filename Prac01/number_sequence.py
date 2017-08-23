import math

x = int(input("Choose an x value "))
y = int(input("Choose a y value "))

print("1. Show the even numbers from {} to {} ".format(x, y))
print("2. Show the odd numbers from {} to {} ".format(x, y))
print("1. Show the squares from {} to {} ".format(x, y))
print("4. Exit the program")

Menu_Selection = int(input())

while Menu_Selection != 4:
    if Menu_Selection == 1:
        for i in range (x, y, 1):
            if i % 2 == 0:
                print(i)
                Menu_Selection = 0
    elif Menu_Selection == 2:
        for i in range (x, y, 1):
            if i % 2 != 0:
                print(i)
                Menu_Selection = 0
    elif Menu_Selection == 3:
        for i in range(x, y, 1):
            if len(str(math.sqrt(i))) < 4:
                print(i)
                Menu_Selection = 0
    else:
        print("1. Show the even numbers from {} to {} ".format(x, y))
        print("2. Show the odd numbers from {} to {} ".format(x, y))
        print("1. Show the squares from {} to {} ".format(x, y))
        print("4. Exit the program")

        Menu_Selection = int(input())

print("Program Ended")

