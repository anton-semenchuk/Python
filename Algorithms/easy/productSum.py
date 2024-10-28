# O(n) time | O(d) space - where d is the depth of the call stack
def productSum(array, multiplier=1):
    total = 0
    for el in array:
        if type(el) is list:
            total += productSum(el, multiplier + 1)
        else:
            total += el
    return multiplier * total


print(productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))
