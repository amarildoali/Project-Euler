result = []
for i in range(34):  # F_34 exceeds 4 million
    f = Algorithms.fibo(i)
    if (f % 2) == 0:
        result.append(f)
print(f"Solution = {sum(result)}")
