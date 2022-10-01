# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 4];
# - [2, 3, 5, 6] => [12, 15]

import random

N = int(input('Введите количество элементов массива: '))
my_list = []
for i in range(N):
    my_list.append(random.randint(0,9))
print(my_list)

new_list = []
x = 0
y = N - 1

if N % 2 == 0:
    for i in my_list:
        if x >= y: 
            break
        else:
            new_list.append(i * my_list[y])
            y -= 1
            x += 1
if N % 2 == 1:
    for i in my_list:
        if x >= y:
            new_list.append(i) 
            break
        else:
            new_list.append(i * my_list[y])
            y -= 1
            x += 1
print(new_list)