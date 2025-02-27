"""
Написать генератор fibonacci, которая принимает номер значения num_count
из чисел Фибоначчи и выводит на экран результат до заданного значения.

Номер значения нужно проверить

Пример:

fibonacci(0) -> raise ValueError('Введите значение больше 1')
fibonacci(5)
1
2
3
5
8
Traceback (most recent call last):
File «C:/Python/Python3/python_generator.py», line 29, in
print(next(fib))
StopIteration
"""


def fibonacci(num_count):
    num_1, num_2 = 0, 1
    for i in range(num_count):
        num_1, num_2 = num_2, num_1 + num_2
        yield num_1
    if num_count < 2:
        raise ValueError('Введите значение больше 1')


for a in fibonacci(5):
    print(a)
