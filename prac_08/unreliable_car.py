from random import randint
from prac_07.car import Car


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_number = randint(1, 100)
        distance_driven = 0
        if random_number < self.reliability:
            distance_driven = super().drive(distance)
        return distance_driven