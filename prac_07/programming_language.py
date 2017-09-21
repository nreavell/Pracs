class programming_language:
    """Represent a Car object."""

    def __init__(self, name='', typing='', reflection = bool, year = ''):
        """Initialise a Car instance.
        fuel: float, one unit of fuel drives one kilometre
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return "{}, {} typing, Reflection={}, First appeared in {}".format(self.name,self.typing,self.reflection,self.year)
    def is_dynamic(self):
        if self.reflection == True:
            return True
        else:
            return False

