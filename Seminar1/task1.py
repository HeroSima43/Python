# Задача 1. Напишите задачу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
# Например:
# 5, 25 -> да
# 4, 16 -> да
# 25, 5 -> да
# 8, 9 -> нет

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
if (a * a == b) or (b * b == a):
    print('Да!')
else:
    print('Нет!')
    