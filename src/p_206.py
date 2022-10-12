"""
Problem 206
"""


def check(number: str) -> bool:
    if number == '1234567890':
        return True
    return False


a = int(10 ** 9)
b = int(1.4 * 10 ** 9)
for i in range(b, a, -10):
    if check(str(i * i)[::2]):
        print(f"Solution = {i}")
        break
