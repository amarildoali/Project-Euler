import math


def triangolare(n):
    return n * (n + 1) / 2


def check_pent(n):
    x = (math.sqrt(24 * n + 1) + 1) / 6
    if x.is_integer():
        return True
    else:
        return False


def check_hex(n):
    x = (math.sqrt(8 * n + 1) + 1) / 4
    if x.is_integer():
        return True
    else:
        return False


for i in range(286, 100000):
    t = triangolare(i)
    if check_pent(t) and check_hex(t):
        print(int(t))
        break
