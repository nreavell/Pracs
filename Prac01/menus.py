Name = input("Enter Name: ")

Menu = input("(H)ello\n(G)oodbye\n(Q)uit\n")

while Menu != "Q":
    if (Menu == "H"):
        print("Hello {}".format(Name))
        Menu = 0
    elif(Menu == "G"):
        print("Goodbye {}".format(Name))
        Menu = 0
    else:
        Menu = input("(H)ello\n(G)oodbye\n(Q)uit\n")

print("Finished")