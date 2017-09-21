"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from prac_07.car import Car


def main():
    """Demo test code to show how to use car class."""
    limo = Car("limo",100)
    limo.add_fuel(20)
    limo.drive(115)
    print(limo)
    print("fuel =", limo.fuel)

    print("{} {}, {}".format(limo.name, limo.fuel, limo.odometer))
    print("{self.name} {self.fuel}, {self.odometer}".format(self=limo))

main()