# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


def randomToOrder(listRN):
    listON = []
    flag = 0
    for i in range(len(listRN)):
        for j in range(len(listRN)):
            if listRN[i] == listRN[j] and i != j:
                flag = 1
                break
        if flag == 0:
            listON.append(listRN[i])
        flag = 0
    return listON
            

originList = [1,2,2,3,4,5,6,7,7,2,8,9,5,5]
print(originList)
listInOrder = randomToOrder(originList)
print(listInOrder)
