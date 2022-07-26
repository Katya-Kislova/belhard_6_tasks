"""
Написать генератор fibonacci, который возвращает подряд значения числе Фибоначчи

Например:

fibonacci_gen = fibonacci()

next(fibonacci_gen) -> 1
next(fibonacci_gen) -> 1
next(fibonacci_gen) -> 2
next(fibonacci_gen) -> 3
next(fibonacci_gen) -> 5
next(fibonacci_gen) -> 8
"""


def fibonacci(n):
    num_1, num_2 = 0, 1
    for i in range(n):
        num_1, num_2 = num_2, num_1 + num_2
        yield num_1


for a in fibonacci(6):
    print(a)
