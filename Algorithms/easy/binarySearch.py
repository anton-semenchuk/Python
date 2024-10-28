# O(log(n)) time | O(1) space
def binarySearch(array, target):
    leftIdx = 0
    rightIdx = len(array) - 1
    while leftIdx <= rightIdx:
        midIdx = (rightIdx + leftIdx) // 2
        if array[midIdx] == target:
            return midIdx
        elif array[midIdx] < target:
            leftIdx = midIdx + 1
        else:
            rightIdx = midIdx - 1
    return False


# O(log(n)) time | O(log(n)) space
def binarySearch2(array, target):
    rightIdx = len(array) - 1
    return binarySearchHelper(array, target, 0, rightIdx)


def binarySearchHelper(array, target, leftIdx, rightIdx):
    if leftIdx > rightIdx:
        return False
    midIdx = (rightIdx + leftIdx) // 2
    if array[midIdx] == target:
        return midIdx
    elif array[midIdx] < target:
        return binarySearchHelper(array, target, midIdx + 1, rightIdx)
    else:
        return binarySearchHelper(array, target, leftIdx, midIdx - 1)


print(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 73))
