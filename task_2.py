# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. 
# Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

from random import randint
n = int(input('Укажите количество элементов в массиве N: '))
list1 = []
for i in range(n):
    # list1.append(i + 1)
    list1.append(randint(1, 10))
print(list1)
x = int(input('Укажите чило x: '))
minDif = abs(x - list1[0])
closeX = list1[0]
for i in range(1, len(list1)):
    dif = abs(x - list1[i])
    if dif <= minDif:
        minDif = dif
        closeX = list1[i]
print(f'Близкий по величине элемент к заданному числу x: {closeX}')

