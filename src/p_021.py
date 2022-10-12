def check_amicable(a):
    b = sum(Algorithms.divisors(a))
    if sum(Algorithms.divisors(b)) == a and a != b:
        return True
    return False


somma = 0
for a in range(1, 10000):
    if check_amicable(a):
        somma += a
print(somma)

### SERVE REFACTORING
