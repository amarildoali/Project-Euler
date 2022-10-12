"""
Problem 25
"""

from algorithms import fibo

for i in range(1, 10 * 1000):
    if len(str(fibo(i))) == 1000:
        print(f"Solution = {i}")
        break

# SERVE REFACTORING
