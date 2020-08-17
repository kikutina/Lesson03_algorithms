#3.	В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

index_min = array[0]
index_max = array[0]

for i in array:
    if i > index_max:
        index_max = i
    elif i < index_min:
        index_min = i
index_min = array.index(index_min)
index_max = array.index(index_max)
array[index_min], array[index_max] = array[index_max], array[index_min]
print(array)