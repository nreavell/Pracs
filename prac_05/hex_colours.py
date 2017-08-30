
COLOUR_CODES = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7",
                "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc",
                "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6",
                "azure1": "#f0ffff", "azure2": "#e0eeee", "beige": "#f5f5dc"}

colour_name = input("Enter a colour: ")

while colour_name != "":
    print("{} is {}".format(colour_name,COLOUR_CODES.get(colour_name)))
    colour_name = input("Enter a colour: ")