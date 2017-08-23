import random

def main():

    GOPHER_POPULATION = 1000
    MIN_DEATH_RATE = 5
    MAX_DEATH_RATE = 25
    MIN_BIRTH_RATE = 10
    MAX_BIRTH_RATE = 20
    DEATH_RATE = random.randrange(MIN_DEATH_RATE,MAX_DEATH_RATE)
    BIRTH_RATE = random.randrange(MIN_BIRTH_RATE,MAX_BIRTH_RATE)

    end_result = calculate_rates(GOPHER_POPULATION, DEATH_RATE, BIRTH_RATE)

    print(end_result)

def calculate_rates(GOPHER_POPULATION, DEATH_RATE, BIRTH_RATE):

    NEW_POPULATION = GOPHER_POPULATION
    GOPHERS_BORN = int(GOPHER_POPULATION * (BIRTH_RATE / 100))
    GOPHERS_DIED = int(GOPHER_POPULATION * (DEATH_RATE /100))

    for years in range(0,10):
        NEW_POPULATION = NEW_POPULATION - GOPHERS_DIED + GOPHERS_BORN
        result = (NEW_POPULATION, GOPHERS_DIED, GOPHERS_BORN)
        return result



main()