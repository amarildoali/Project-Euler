def a():
    x = sum(list(range(101)))
    return x * x


def b():
    return sum([x * x for x in range(101)])


print(a() - b())
