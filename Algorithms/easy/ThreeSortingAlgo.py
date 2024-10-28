# three function have O(n^2) time | O(1) space
def insertionSort(arr):
    for idx in range(1, len(arr)):
        i = idx
        while i > 0 and arr[i] < arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1
    return arr


def bubbleSort(arr):
    isSorted = False
    counter = 0
    while not isSorted:
        isSorted = True
        for i in range(len(arr) - 1 - counter):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                isSorted = False
        counter += 1
    return arr


def selectionSort(array):
    currentIdx = 0
    while currentIdx < len(array) - 1:
        smallestNumIdx = currentIdx
        for i in range(currentIdx + 1, len(array)):
            if array[i] < array[smallestNumIdx]:
                smallestNumIdx = i
        swap(array, currentIdx, smallestNumIdx)
        currentIdx += 1
    return array


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


print(selectionSort([4, 2, 6, 3, 7, 19, 1, 0]))