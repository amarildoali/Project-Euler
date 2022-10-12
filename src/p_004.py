def is_palindrome(n):
    a = str(n)
    b = a[len(a):: -1]
    return bool(a == b)


result = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        if (i * j) > result and is_palindrome(i * j):
            result = i * j
print(f"Solution = {result}")
