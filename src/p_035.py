from algorithms import primes


def slitta(numero):
    return numero[1:] + numero[0]


def circolare(n, primi):
    for _ in range(len(n)):
        if int(n) not in primi:
            return 0
        n = slitta(n)
    return 1


if __name__ == "__main__":
    primi = primes(10 ** 6)
    s = 0
    for i in primi:
        s += circolare(str(i), primi)
    print(s)

# SERVE REFACTORING
