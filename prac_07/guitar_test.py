from prac_07.guitar import Guitar

def main():
    """Demo test code to show how to use car class."""
    cool = Guitar('johnson', '1997', "1234.45")
    cool2 = Guitar('johnson', '1947', "1234.45")
    print(cool2.get_age())
    print("{} is_vintage() - Expected True - Get {}".format(cool2.name, cool2.is_vintage()))
    print("{} is_age() - Expected 70 - Get {}".format(cool2.name, cool2.get_age()))
main()