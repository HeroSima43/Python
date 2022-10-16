# Напишите программу, которая принимает на вход число N
# и выдает последовательность из N членов.
# Пример: Для N = 5: 1, -3, 9, -27, 81

number = int(input('Введите N: '))
# z = 1
# print(z, end=', ')
# for i in range(number - 1):
#     z = z * (-3)
#     print(z, end=', ')


my_list = [(-3)**i for i in range(number)]
print(f"Итоговая последовательность после применения list comprehension: {my_list}")
