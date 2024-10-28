# O(n*n^2) time | O(n*n^2) space
def powerset(array):
    subsets = [[]]
    for el in array:
        for i in range(len(subsets)):
            currentSubset = subsets[i]
            subsets.append(currentSubset + [el])
    return subsets


# O(n*n^2) time | O(n*n^2) space
def powerset2(array, idx=None):
    if idx is None:
        idx = len(array) - 1
    elif idx < 0:
        return [[]]
    el = array[idx]
    subsets = powerset2(array, idx - 1)
    for i in range(len(subsets)):
        currentSubset = subsets[i]
        subsets.append(currentSubset + [el])
    return subsets


print(powerset2([1, 2, 3, 4]))