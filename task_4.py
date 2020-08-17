#4.	Определить, какое число в массиве встречается чаще всего.

import random


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 3
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

array_1 = set(array)

a = None
num = 0

for item in array_1:
    num_often = array.count(item)
    if num_often > num:
        num = num_often
        a = item

print(f'Число {a} встречается чаще всего,  {array.count(a)} раза')
