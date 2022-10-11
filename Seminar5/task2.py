# Дан список чисел. Создайте список, в который попадают числа,
# описываемые возрастащую последовательность. Порядок элементов менять нельзя.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] -> [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

my_list = [1, 5, 2, 3, 4, 6, 1, 7]

def nextmax(my_list):
    max = my_list[0]
    res = [my_list[0]]
    for i in range(len(my_list)):
        if my_list[i] > max:
            max = my_list[i]
            res.append(max)

    return res

print(nextmax(my_list))
