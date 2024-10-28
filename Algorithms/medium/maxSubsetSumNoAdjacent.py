# O(n) time | O(1) space
def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return None
    elif len(array) == 1:
        return array[0]
    first = array[0]
    second = max(array[0], array[1])
    for i in range(2, len(array)):
        current = max(second, first + array[i])
        first = second
        second = current
    return second


# O(n) time | O(n) space
def maxSubsetSumNoAdjacent1(array):
    if not len(array):
        return None
    elif len(array) == 1:
        return array[0]
    maxSum = array[:]
    maxSum[1] = max(array[0], array[1])
    for i in range(2, len(array)):
        maxSum[i] = max(maxSum[i - 1], maxSum[i] + maxSum[i - 2])
    return maxSum[-1]


arr = [7, 10, 12, 7, 9, 14]
print(maxSubsetSumNoAdjacent(arr))