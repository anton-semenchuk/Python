# O(n) time | O(1) space
def isMonotonicArray(array):
    isNonIncreasing = True
    isNonDecreasing = True
    for i in range(1, len(array)):
        if array[i] > array[i - 1]:
            isNonIncreasing = False
        if array[i] < array[i - 1]:
            isNonDecreasing = False
    return isNonIncreasing or isNonDecreasing


# O(n) time | O(1) space
def isMonotonicArray2(array):
    sign = '+' if array[0] < array[-1] else '-'
    for i in range(len(array) - 1):
        if sign == '+':
            if array[i] <= array[i + 1]:
                continue
            return False
        elif sign == '-':
            if array[i] >= array[i + 1]:
                continue
            return False
    return True


print(isMonotonicArray([-1, -5, -10, -1100, -1100, -1101, -1102, -9001]))