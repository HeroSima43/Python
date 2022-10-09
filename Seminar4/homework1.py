# Вычислить число с заданой точностью d.
# Например: при d = 0.001, pi = 3.141

from math import pi


d = float(input('Введите точность: '))

count = 0
while d < 1:
    d *= 10
    count += 1
print(round(pi, count))
