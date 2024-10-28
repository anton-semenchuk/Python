# return True if we visit every element only once and return to the first element
# O(n) time | O(1) space
def hasSingleCycle(arr):
    currentIdx = 0
    numElementsVisited = 0
    while numElementsVisited < len(arr):
        if numElementsVisited > 0 and currentIdx == 0:
            return False
        numElementsVisited += 1
        currentIdx = getNextIdx(currentIdx, arr)
    return currentIdx == 0


def getNextIdx(currentIdx, arr):
    jump = arr[currentIdx]
    nextIdx = (currentIdx + jump) % len(arr)
    return nextIdx if nextIdx >= 0 else nextIdx + len(arr)


print(hasSingleCycle([2, 3, 1, -4, -4, 2]))