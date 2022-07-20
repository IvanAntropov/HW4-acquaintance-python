# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# работает только с пробелами 

path1 = 'polynomial1.txt'
path2 = 'polynomial2.txt'
path3 = 'result.txt'

def multiOfPolynomial(poly1, poly2): 
    a1 = int(poly1[0][:-3])
    a2 = int(poly2[0][:-3])
    b1 = int(poly1[1] + poly1[2][:-1])
    b2 = int(poly1[1] + poly2[2][:-1])
    c1 = int(poly1[3] + poly1[4])
    c2 = int(poly1[3] + poly2[4])
    a = str(a1 + a2) 
    b = str(b1 + b2)
    if int(b) > 0:
        b = ' + ' + b
    else:
        b = ' - ' + b[1:]
    c = str(c1 + c2)
    if int(c) > 0:
        c = ' + ' + c
    else:
        c = ' - ' + c[1:]
    summa = a + 'x^2' + b + 'x' + c + ' = 0' #не знаю нужен ли ноль, но добавил везде
    return summa

with open(path1, 'r') as p1:
    p1 = p1.readline()
    p1 = p1.split()

with open(path2, 'r') as p2:
    p2 = p2.readline().split()
    p2 = p2.split()

with open(path3, 'w') as p:
    p.write(multiOfPolynomial(p1,p2))

print(multiOfPolynomial(p1,p2))
