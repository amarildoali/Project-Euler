def is_pitagora(a, b, c):
    if (a * a + b * b) == (c * c):
        return True
    return False


def find_triangle():
    for a in range(1, 1000):
        for b in range(a, 1000):
            if a + b > 1000:
                continue
            for c in range(b, 1000):
                if (a + b + c) == 1000 and is_pitagora(a, b, c):
                    print(f"Solution = {a * b * c}")
                    return


find_triangle()
