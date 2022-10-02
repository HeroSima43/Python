# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

fib1 = 1
fib2 = -1
fib_negative = []
fib_negative.append(fib1)
fib_negative.append(fib2)

n = int(input('Введите n: '))

for i in range(-n, -2):
    fib1, fib2 = fib2, fib1 - fib2
    fib_negative.append(fib2)

fib_negative.reverse()
fib_negative.append(0)

fib1 = fib2 = 1
fib_negative.append(fib1)
fib_negative.append(fib2)

for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    fib_negative.append(fib2)
print(fib_negative)