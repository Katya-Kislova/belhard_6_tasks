"""
Написать замыкание.

Написать функцию add_numb, которая должна принимать некоторое целое число.
Написать внутри функции add_numb функцию inner, которая также принимает
целое число и возвращает сумму чисел, которое принимает она и которое
принимает функция add_numb.

Пример:
add_two = add_numb(2)
add_two(3)  # 5

add_three = add_numb(3)
add_three(3) # 6
"""


def add_numb(n: int):
    def inner(y: int):
        return y + n
    return inner


sum_def = add_numb(5)
print(sum_def(11))
