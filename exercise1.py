# Вычислить число c заданной точностью d
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$ and 10**(-1) <= number and number <= 10**(-10)

import math

def inputValue(text: str):
    check = False
    while not check:
        try:
            number = int(input(text))
            check = True
        except ValueError:
            print('Try again: ')
            number = int(input(text))
    return number
              

numberOfRound = inputValue('Enter number of round up: ')
roundNumber = round(math.pi,numberOfRound)
print(roundNumber)