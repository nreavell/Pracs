"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
result = 0
while not finished:
    try:
        result = int(input("Please input an integer: \n"))
        finished = True
    except ValueError:
          print("Error: invalid integer. \n")
print("Valid result is:", result)