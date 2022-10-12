def giorni_del_mese(m, a):
    if m in (4, 6, 9, 11):
        return 30
    elif m == 2:
        if (a % 100 == 0 and a % 400 == 0) or (a % 100 != 0 and a % 4 == 0):
            return 29
        else:
            return 28
    else:
        return 31


conteggio = 0
L = 2  # perchè 1 Gen 1901 è Martedi in base a come è stato dato il problema
for a in range(1901, 2001):
    for m in range(1, 13):
        for g in range(1, giorni_del_mese(m, a) + 1):
            if L == 7:
                if g == 1:
                    conteggio += 1
                L = 1
            else:
                L += 1
print(conteggio)

# SERVE REFACTORING
