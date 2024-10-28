# O(nLog(n) + nLog(m)) time | O(1) space - where n and m are the length of the arrays
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    idxOne, idxTwo = 0, 0
    smallest = float("inf")
    current = float("inf")
    smallestPair = []
    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        firstNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]
        if firstNum < secondNum:
            current = secondNum - firstNum
            idxOne += 1
        elif secondNum < firstNum:
            current = firstNum - secondNum
            idxTwo += 1
        else:
            return [arrayOne[idxOne], arrayTwo[idxTwo]]
        if current < smallest:
            smallest = current
            smallestPair = [firstNum, secondNum]
    return smallestPair


print(smallestDifference([-1, 3, 5, 10, 20, 28], [15, 17, 26, 134, 135]))