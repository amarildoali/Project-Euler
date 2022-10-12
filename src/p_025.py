from algorithms import fibo

for i in range(1, 10 * 1000):
    s = fibo(i).__str__()
    if s.__len__() == 1000:
        print(i)
        break

# SERVE REFACTORING
