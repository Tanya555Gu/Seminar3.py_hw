# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. 
# Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

from random import randint
N = int(input('Укажите количество элементов в массиве N: '))
A = []
for i in range (N):
    A.append(randint(-10, 10))
print(A)
X = int(input('Укажите чило X: '))
countX = 0
for num in A:
    if num == X:
        countX += 1
print(f'Количество повторений числа {X} в массиве -> {countX}')







