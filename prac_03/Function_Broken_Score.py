"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

def main():

    score = float(input("Enter score: "))

    result = get_result(score)
    print(result)

def get_result(score):

    if 90 > score >= 50:
        result = "Passable"
    elif 100 >= score >= 90:
        result = "Excellent"
    elif 0 <= score < 50:
        result = "Bad"
    else:
        result = "invalid score"

    return result


main()