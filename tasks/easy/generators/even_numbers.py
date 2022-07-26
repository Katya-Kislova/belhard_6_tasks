"""
Написать генератор get_even_number, который возвращает подряд четные числа

Например:

even_gen = get_even_number()

next(even_gen) -> 2
next(even_gen) -> 4
next(even_gen) -> 6
"""


def get_even_number(n):
    number = 2
    while number <= n:
        yield number
        number += 2


for i in get_even_number(10):
    print(i)
