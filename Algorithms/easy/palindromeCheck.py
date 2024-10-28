# O(n) time | O(1) space
def palindromeCheck(string):
    leftPointer = 0
    rightPointer = len(string) - 1
    while leftPointer < rightPointer:
        if string[leftPointer] == string[rightPointer]:
            leftPointer += 1
            rightPointer -= 1
            continue
        return False
    return True


print(palindromeCheck('abcdcba'))