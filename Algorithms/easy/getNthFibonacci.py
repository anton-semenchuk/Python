# O(2^n) time | O(n) space
def getNthFib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return getNthFib(n - 1) + getNthFib(n - 2)


# O(n) time | O(1) space
def getNthFib2(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    counter = 3
    first = 0
    second = 1
    while counter <= n:
        first, second = second, first + second
        counter += 1
    return second


print(getNthFib2(7))