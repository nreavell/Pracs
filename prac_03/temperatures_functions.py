"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

def main():

    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius_input = float(input("Celsius: "))
            fahrenheit = Celcius_to_Fahrenheit(celsius_input)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit_input = float(input("Fahrenheit: "))
            celsius = Fahrenheit_to_Celcius(fahrenheit_input)
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def Fahrenheit_to_Celcius(fahrenheit_input):
    celsius = 5 / 9 * (fahrenheit_input - 32)
    return celsius


def Celcius_to_Fahrenheit(celcius_input):
    fahrenheit = celcius_input * 9.0 / 5 + 32
    return fahrenheit


main()