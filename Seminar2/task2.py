# Для натурального N создать словарь индекс значение, состоящий из элементов последовательности 3n + 1.
# Пример: Для N = 6: (4, 7, 10, 13, 16, 19)
N = int(input('Введите N: '))
for i in range(N):
    z = 3 * (i + 1) + 1
    print(z, end=', ')