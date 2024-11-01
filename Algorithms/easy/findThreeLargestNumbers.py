# O(n) time | O(1) space
def findThreeLargestNumbers(array):
    threeLargest = [array[0], array[1], array[2]]
    for i in range(3, len(array)):
        num = array[i]
        minIdx = threeLargest.index(min(threeLargest[0], threeLargest[1], threeLargest[2]))
        if num > threeLargest[minIdx]:
            threeLargest[minIdx] = num
    return threeLargest


# O(n) time | O(1) space
def findThreeLargestNumbers2(array):
    threeLargest = [None, None, None]
    for num in array:
        updateLargest(threeLargest, num)
    return threeLargest


def updateLargest(threeLargest, num):
    if threeLargest[2] is None or num > threeLargest[2]:
        shiftAndUpdate(threeLargest, num, 2)
    elif threeLargest[1] is None or num > threeLargest[1]:
        shiftAndUpdate(threeLargest, num, 1)
    elif threeLargest[0] is None or num > threeLargest[0]:
        shiftAndUpdate(threeLargest, num, 0)


def shiftAndUpdate(threeLargest, num, idx):
    for i in range(idx + 1):
        if i == idx:
            threeLargest[i] = num
        else:
            threeLargest[i] = threeLargest[i + 1]


print(findThreeLargestNumbers2([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]))
