# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

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
              
def SimpleMultipliers(number):
    listMulti = []
    numberMulti = 2
    while abs(number) != 1: # помимо натуральных считате целые 
        if number%numberMulti == 0:
            number = number/numberMulti
            listMulti.append(numberMulti)
            numberMulti = 2
        else:
            numberMulti+=1
    return listMulti

numberN = inputValue('Enter number: ')
listOfMulipliers = SimpleMultipliers(numberN)
print(f'{listOfMulipliers}')