from prac_07.programming_language import programming_language

def main():
    """Demo test code to show how to use car class."""
    ruby = programming_language("ruby", "Dynamic", True, 1995)
    python = programming_language("python", "Dynamic", True, 1991)
    visual_basic = programming_language("Visual Basic", "Static", False, 1991)
    list = [ruby, python, visual_basic]

    dynamic_list = []
    print("The dynamically typed languages are:")
    for language in list:
        if language.is_dynamic() == True:
            dynamic_list += [language]
            print(language.name)
main()