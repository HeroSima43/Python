# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока
# делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента
# достаются сделавшему последний ход. Сколько конфет нужно взять
# первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint


def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. На столе осталось {value} конфет.")


first_player = input("Введите имя первого игрока: ")
second_player = input("Введите имя второго игрока: ")
value = int(input("Введите количество конфет на столе: "))
flag = randint(0, 1)
if flag:
    print(f"Первый ходит {first_player}")
else:
    print(f"Первый ходит {second_player}")

counter1 = 0
counter2 = 0

while value > 28:
    if flag:
        k = input_dat(first_player)
        counter1 += k
        value -= k
        flag = False
        p_print(first_player, k, counter1, value)
    else:
        k = input_dat(second_player)
        counter2 += k
        value -= k
        flag = True
        p_print(second_player, k, counter2, value)

if flag:
    print(f"Выиграл {first_player}")
else:
    print(f"Выиграл {second_player}")
