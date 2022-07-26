"""
Написать генератор factorial, который возвращает подряд значения факториала

Например:

factorial_gen = factorial()

next(factorial_gen) -> 1
next(factorial_gen) -> 2
next(factorial_gen) -> 6
next(factorial_gen) -> 24
"""


def factorial(n=1):
    # num = 1
    # for i in range(1, n + 1):
    #     num *= i
    #     yield num
    result = 1
    while n >= 1:
        result *= n
        yield result
        n += 1


for i in factorial(5):
    print(i)
