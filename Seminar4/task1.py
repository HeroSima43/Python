# Задайте строку из набора чисел. Напишите программу,
# которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.
nums = "1 2 3 4 67    5 6"
my_list = [int(num) for num in nums.split()]
print(max(my_list), min(my_list))
