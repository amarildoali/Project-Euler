def alto_destra(x):
    return 4 * x * x + 4 * x + 1


def basso_destra(x):
    return 4 * x * x - 2 * x + 1


def basso_sinistra(x):
    return 4 * x * x + 1


def alto_sinistra(x):
    return 4 * x * x + 2 * x + 1


somma = 1
for i in range(1, 501):
    somma += alto_destra(i)
    somma += basso_destra(i)
    somma += alto_sinistra(i)
    somma += basso_sinistra(i)
print(somma)

### SERVE REFACTORING
