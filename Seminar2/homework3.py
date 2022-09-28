# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
# Пример: Для N = 6 [2, 2, 2, 2, 2, 3] -> 13
N = int(input('Введите N: '))
list = []
for i in range(N):
    list.append(round((1 + 1/(i + 1))**(i + 1)))
print(list)
sum = 0
for i in list:
    sum += i
print(f'Сумма чисел последовательности равна:', sum)
