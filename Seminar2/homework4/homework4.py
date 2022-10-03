# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

import random

N = int(input('Введите N: '))
list = []
for i in range(N):
    list.append(random.randint(-N, N))
print(list)

pro = 1

data = open('file.txt', 'r')
for i in data:
    pro = pro * list[int(i)]
print(f'Произведение элементов {list[1]} и {list[3]} равно: {pro}')
data.close()
