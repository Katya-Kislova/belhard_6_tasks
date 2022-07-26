"""
Написать функцию triangular_sequence, которая принимает n и возвращает
последовательность следующего вида:

1
22
333
4444
55555
...

Например:

n = 3:
1
22
333

n = 6:
1
22
333
4444
55555
666666
"""


def triangular_sequence(n: int, result: int = 1):
    if n >= result:
        print(str(result) * result)
        return triangular_sequence(n, result + 1)


print(triangular_sequence(4))
