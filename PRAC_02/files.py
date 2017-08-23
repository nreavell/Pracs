# Program for inputting a name and printing to 'name.txt'

# NAME = input("What is your name? ")
# DATAFILE = "name.txt"
# OUT_DATAFILE = open(DATAFILE, 'w')
# print(NAME, file=OUT_DATAFILE)
# OUT_DATAFILE.close()

# Program for reading 'name.txt' and displaying the contents
# DATAFILE = "name.txt"
# IN_DATAFILE = open(DATAFILE, 'r')
# print(IN_DATAFILE.readline())
#
# IN_DATAFILE.close()

# Program for adding numbers in a file list
NUMBERFILE = "numbers.txt"
IN_NUMBERFILE = open(NUMBERFILE, 'r')
result = 0

for line in IN_NUMBERFILE:
        result += int(line)

print(result)