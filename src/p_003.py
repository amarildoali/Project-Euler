divisors = Algorithms.divisors(600851475143)
result = []
for i in divisors:
    if Algorithms.is_prime(i):
        result.append(i)
print(f"Solution = {max(result)}")
