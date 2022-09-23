# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

from math import sqrt

x1 = int(input('Введите координату X первой точки: '))
y1 = int(input('Введите координату Y первой точки: '))
x2 = int(input('Введите координату X второй точки: '))
y2 = int(input('Введите координату Y второй точки: '))
d = sqrt((x1 - x2)**2 + (y1 - y2)**2)
print('Расстояние между точками равно: ', round(d, 2))