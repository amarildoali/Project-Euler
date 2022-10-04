def divisible(n):
    for divisor in range(11, 21):
        if n % divisor != 0:
            return False
    return True


i = 1
while True:
    if divisible(i):
        print(i)
        break
    i += 1
