# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

from array import array


with open('file1.txt', 'r') as file1:
    text1 = str(file1.read())

with open('file2.txt', 'r') as file2:
    text2 = str(file2.read())

print(text1, text2)

x = text1.split(' + ')
x2 = text2.split(' + ')

print(x, x2)


def func(array: list):
    if 'x^2' not in array[0]:
        array.insert(0, '0')
    if 'x' not in array[1]:
        array.insert(1, '0')
    if len(array) == 2:
        array.append('0')
    return array


x = func(x)
x2 = func(x2)


def func2(array: list):
    new_array = []
    for i in array:
        if '*x^2' in i:
            new_array.append(int(i.replace('*x^2', '')))
        elif '*x' in i:
            new_array.append(int(i.replace('*x', '')))
        else:
            new_array.append(int(i))
    return new_array

print(x, x2)
array1 = func2(x)
array2 = func2(x2)
print(array1, array2)

text = str(array1[0] + array2[0]) + ' + ' + str(array1[1] + array2[1]) + ' + ' + str(array1[2] + array2[2])

with open('file3.txt', 'w') as file3:
    text3 = file3.write(text)