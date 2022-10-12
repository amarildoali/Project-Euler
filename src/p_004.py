"""
Problem 4
"""


def is_palindrome(number):
    normal = str(number)
    normal_reversed = normal[len(normal):: -1]
    return bool(normal == normal_reversed)


result = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        if (i * j) > result and is_palindrome(i * j):
            result = i * j
print(f"Solution = {result}")
