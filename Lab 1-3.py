from random import randint
n = int(input(" Введите размер масива "))
array  = []
for i in range(n):
    array.append(randint(-10, 10))
print("Массив", array)
avg = 0
oddCount = 0
for i in range(n):
    if array[i] % 2 == 0:
        avg += array[i]
        oddCount += 1
avg /= oddCount
print("Среднее арифметическое целых чисел", avg)
for i in range(n):
    i = n - i - 1
maxEl = -10
for i in range(n):
    if array[i] < 0 and array[i] > maxEl:
        maxEl = array[i]
print("Максимальный отрицательный элемент массива", maxEl)
print("Ненулевые элементы массива в обратном направлении")
for i in range(n):
    i = n - i - 1
    if not array[i] == 0:
        print(array[i])



