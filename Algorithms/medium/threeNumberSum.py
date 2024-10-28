# O(n^2) time | O(n) space
def threeNumberSum(array, targetSum):
    resultingArray = []
    array.sort()
    for idx in range(len(array) - 2):
        leftPointer = idx + 1
        rightPointer = len(array) - 1
        while leftPointer < rightPointer:
            currentSum = array[idx] + array[leftPointer] + array[rightPointer]
            if currentSum < targetSum:
                leftPointer += 1
            elif currentSum > targetSum:
                rightPointer -= 1
            elif currentSum == targetSum:
                resultingArray.append([array[idx], array[leftPointer], array[rightPointer]])
                leftPointer += 1
                rightPointer -= 1
    return resultingArray


print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))