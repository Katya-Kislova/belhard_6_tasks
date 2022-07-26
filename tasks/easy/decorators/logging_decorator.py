"""
Написать функцию hello, которая принимает аргумент name - строку с именем и
выводит принтом "Привет, {name}"

Написать декоратор log_decorator, который перед выполнением
функции печатает на экран строку, вида
"Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}".
После выполнения функции напечатать строку "Выполнено {func.__name__}"
"""


def log_decorator(function):
    def wrapper(*args, **kwargs):
        print("Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}")
        result = function(*args, **kwargs)
        print("Выполнено {func.__name__}")
        return result
    return wrapper


@log_decorator
def hello(name):
    print(f'Привет, {name}')
