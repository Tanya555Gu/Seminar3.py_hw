# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. 
# Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

from random import randint
N = int(input('Укажите количество элементов в массиве N: '))
A = []
for i in range(N):
    # A.append(i + 1)
    A.append(randint(1, 10))
print(A)
X = int(input('Укажите чило X: '))
minDif = abs(X - A[0])
closeX = A[0]
for i in range(1, len(A)):
    dif = abs(X - A[i])
    if dif <= minDif:
        minDif = dif
        closeX = A[i]
print(f'Близкий по величине элемент к заданному числу X: {closeX}')

