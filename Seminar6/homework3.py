# Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# import random

# N = int(input('Введите количество элементов массива: '))
# my_list = []

# for i in range(N):
#     my_list.append(round(random.uniform(0,100), 2))
# print(f'Исходный массив: {my_list}')

# count = 0

# for i in my_list:
#     while my_list[count] > 1:
#         my_list[count] +=  - 1
#     else:
#         count += 1
# print(f'Измененный массив: {my_list}')

# count = 0
# list_max = my_list[count]
# for i in my_list:
#     if i > list_max:
#         list_max = i
# print(f'Максимальное значение дробной части: {round(list_max, 2)}')

# count = 0
# list_min = my_list[count]
# for i in my_list:
#     if i < list_min:
#         list_min = i
# print(f'Минимальное значение дробной части: {round(list_min, 2)}')

# print(f'Разницу между максимальным и минимальным значением дробной части
# элементов равно: {round((list_max - list_min), 2)}')


my_list = list(map(float, input("Введите числа через пробел:\n").split()))
new_list = [round(i % 1, 2) for i in my_list if i % 1 != 0]
print(max(new_list) - min(new_list))
