"""
Написать рекурсивную функцию check_number, которая должна возвращать True,
если переданное ей число n является степенью двойки (1 тоже степень двойки) и
False, если нет

Нельзя пользоваться операцией возведения в степень
"""


def check_number(n):
    if n / 2 >= 1:
        return check_number(n / 2)
    elif n == 1.0:
        return True
    else:
        return False


print(check_number(32))
