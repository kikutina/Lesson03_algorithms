# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и
# «максимальный отрицательный». Это два абсолютно разных значения.

import random


SIZE = 20
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

i = 0
index_num = -1

while i < SIZE:
    if array[i] < 0 and index_num == -1:
        index_num = i
    elif array[i] < 0 and array [i] > array[index_num]:
        index_num = i
    i += 1

print(f'Максимальный отрицательный элемент {array[index_num]} : позиция {index_num}')
