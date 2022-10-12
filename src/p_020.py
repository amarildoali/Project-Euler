from math import factorial

NUMBER = str(factorial(100))
result = 0
for i in NUMBER:
    result += int(i)
print(f"Solution = {result}")
