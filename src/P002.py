from src import Algorithms

result = []
for i in range(34):  # F_34 exceeds 4 million
    f = Algorithms.fibo(i)  # O(n)
    if (f % 2) == 0:
        result.append(f)
print(f"Solution = {sum(result)}")
print("Complexity = O(n^2)")
