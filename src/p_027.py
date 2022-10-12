from algorithms import is_prime


def numero_di_primi(s):
    x = 0
    for i in s:
        if is_prime(i):
            x += 1
        else:
            return x


def funzione(n, a, b):
    return n * n + a * n + b


massimo, A, B = 0, 0, 0
for a in range(-999, 1000):
    for b in range(-999, 1001, 2):
        successione = []
        for n in range(100):
            successione.append(funzione(n, a, b))
        primi_di_fila = numero_di_primi(successione)
        if primi_di_fila > massimo:
            massimo = primi_di_fila
            print("MAX: " + massimo.__str__() + "\t\t\tA:" +
                  a.__str__() + "\tB:" + b.__str__())
            A = a
            B = b
print(A * B)

# SERVE REFACTORING
