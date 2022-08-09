# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


import random

k = 2

a = random.randint(-100, 100)
b = random.randint(-100, 100)
c = random.randint(-100, 100)

array = []

if a != 0:
    array.append(f'{a}*x^{k}')

if b != 0:
    if b < 0:
        array.append(f' (-{abs(b)}*x)')
    else:
        array.append(f'{b}*x')

if c != 0:
    if c < 0:
        array.append(f'(-{abs(c)})')
    else:
        array.append(f'{c}')

x = ''
for i in range(0, len(array)):
    if i != len(array) - 1:
        x = x + array[i] + ' + '
    else:
        x = x + array[i] + ' = 0'

with open('file.txt', 'w') as f:
    f.write(x)

print(array)
print(x)
