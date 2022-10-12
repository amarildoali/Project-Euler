"""
Problem 3
"""

from algorithms import divisors, is_prime

divisors = divisors(600851475143)
result = []
for i in divisors:
    if is_prime(i):
        result.append(i)
print(f"Solution = {max(result)}")
