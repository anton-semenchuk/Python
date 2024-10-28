# O(n) time | O(1) space
def kadanesAlgorithm(arr):
    maxEndingHere = arr[0]
    maxSoFar = arr[0]
    for num in arr[1:]:
        maxEndingHere = max(num, maxEndingHere + num)
        maxSoFar = max(maxSoFar, maxEndingHere)
    return maxSoFar


print(kadanesAlgorithm([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]))
