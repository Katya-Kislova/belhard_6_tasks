"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""


def yes_or_no(some_list):
    if len(some_list) > len(set(some_list)):
        print('Yes')
    else:
        print('No')


print(yes_or_no([1, 334, 24, 54, 11, 1, 45, 44]))
