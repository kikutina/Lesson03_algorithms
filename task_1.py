#В диапазоне натуральных чисел от 2 до 99 определить,
#сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

result = {}
for a in range(2, 10):
    result[a] = []
    for i in range(2, 100):
        if i % a == 0:
            result[a].append(i)
    print(f'{a} - {len(result[a])}')