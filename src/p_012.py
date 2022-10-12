from algorithms import divisors

for i in range(10 ** 1000):
    t = i * (i + 1) / 2
    if len(divisors(t)) > 500:
        print(int(t))
        break

# SERVE REFACTORING
