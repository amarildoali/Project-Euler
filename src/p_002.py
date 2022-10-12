"""
Problem 2
"""

from algorithms import fibo

result = []
for i in range(34):  # F_34 exceeds 4 million
    FIBO_I = fibo(i)
    if (FIBO_I % 2) == 0:
        result.append(FIBO_I)
print(f"Solution = {sum(result)}")
