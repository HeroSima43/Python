# Задача 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Например:
# 1, 4, 8, 7, 5 - > 8

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
d = int(input('Введите четвертое число: '))
e = int(input('Введите пятое число: '))
numbers = [a,b,c,d,e]
max = a
for i in numbers:
    if i > max:
        max = i
print('Максимальное число: ', max)

