#  Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
#  Пример:
#  - 6782 -> 23
#  - 0,56 -> 11
number = float(input('Введите вещественное число: '))
z = str(number)
print(z)
list = []
for i in range(len(z)):
    list.append(z[i])
print('Заполненный массив из строк:', list)
for i in list:
    if i == '.':
        list.remove(i)
print('Измененный массив:', list)
sum = 0
for i in list:
    sum += int(i)
print(f'Сумма цифр числа {number} равна:', sum)
