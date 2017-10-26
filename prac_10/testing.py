import doctest
from prac_07.car import Car


def repeat_string(s, n):
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than given length
    >>> is_long_word("not")
    False
    >>> is_long_word("ThisIsABigWord")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("kwl", 3) == "kwl kwl"

    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"

    # 2. write assert statements to show if Car sets the fuel correctly
    # Note that Car's __init__ function sets the fuel in one of two ways:
    # using the value passed in or the default
    # You should test both of these
    test_car = Car(fuel=10)
    assert test_car.fuel == 10

    test_car = Car()
    assert test_car.fuel == 0


# 5. Write and test a function to format a phrase as a sentence,
# starting with a capital and ending with a single full stop.
# Important: start with a function header and just use pass as the body
# then add doctests so that:
# 'hello' -> ''Hello.'
# 'It is an ex parrot.' -> 'It is an ex parrot.'
# and one more you decide (that's valid!)
# then write the body of the function so that the tests pass

def phrase_to_sentence(phrase):
    sentence = phrase.capitalize()
    if sentence[-1] != '.':
        sentence += '.'
    return sentence


run_tests()

doctest.testmod()