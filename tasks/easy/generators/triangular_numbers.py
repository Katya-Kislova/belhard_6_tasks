"""
Написать генератор triangular_numbers, который возвращает подряд числа
треугольные числа


Формула:
Tn = 1 / 2 * n * (n + 1)


Например:
tn_gen = triangular_numbers()

next(tn_gen) -> 1
next(tn_gen) -> 3
next(tn_gen) -> 6
next(tn_gen) -> 10
next(tn_gen) -> 15
next(tn_gen) -> 21
"""


def triangular_numbers(n=1):
    while n > 0:
        yield 1 / 2 * n * (n + 1)
        n += 1


for a in triangular_numbers(3):
    print(a)
