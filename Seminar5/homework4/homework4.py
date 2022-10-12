# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res


def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res


path_1 = 'Seminar5/homework4/file_1.txt'
data = open(path_1, 'r')
for line in data:
    a = coding(line)
data.close()

with open('Seminar5/homework4/file_2.txt', 'w') as data:
    data.write(a + '\n')

path_1 = 'Seminar5/homework4/file_1.txt'
data = open(path_1, 'r')
for line in data:
    b = decoding(coding(line))
data.close()

with open('Seminar5/homework4/file_2.txt', 'a') as data:
    data.write(b)
