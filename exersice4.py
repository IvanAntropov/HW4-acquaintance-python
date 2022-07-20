# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0   

import random
path = 'polynomial.txt'

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

def makeRandomList(min,max):
    randomList = []
    j = 0
    for i in range(3):
        j = 0
        number = random.randrange(min,max)
        randomList.append(number)
        while j != i+1:
            if randomList[i] == randomList[j] and i != j:
                number = random.randrange(min,max)
                randomList[i] = number
                j = -1
            j+=1
    return randomList

def makePoly(listR, numberK):
    string = ''
    stringList = [f'{listR[0]}x^{numberK}', f'{listR[1]}x', f'{listR[2]}']
    if listR[0] > 0:
        string = stringList[0]
    if listR[1] > 0 and listR[0] > 0:
        string = string + ' + ' + stringList[1]
    elif listR[1] > 0 and listR[0] == 0:
        string = string + stringList[1]
    if listR[2] > 0:
        string = string + ' + ' + stringList[2]
    string = string + ' = 0' + '\n' 
    return string

numberK = inputValue('Enter k coefficient: ')
polynomial = makeRandomList(0,3)
forFile = makePoly(polynomial, numberK = 2)

print(makePoly(polynomial, numberK = 2))

with open(path, 'a') as p:
    p.write(forFile)

