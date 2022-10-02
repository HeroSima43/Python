# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

N = int(input('Введите число: '))
my_list = []
while N > 0:
    ostatok = N % 2
    N = N // 2
    my_list.append(ostatok)
my_list.reverse()
print(my_list)
