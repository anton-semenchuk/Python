# O(n) time | O(1) space)
def moveElementToEnd(array, toMove):
    for i in range(len(array) - 2, -1, -1):
        k = i
        j = i + 1
        while array[k] == toMove and array[j] != toMove:
            array[k], array[j] = array[j], array[k]
            k += 1
            j += 1
    return array


def moveElementToEnd2(array, toMove):
    j = len(array) - 1
    i = 0
    while i < j:
        while i < j and array[j] == toMove:
            j -= 1
        if array[i] == toMove:
            array[i], array[j] = array[j], array[i]
        i += 1
    return array


print(moveElementToEnd([2, 1, 2, 2, 2, 3, 4, 2], 2))
