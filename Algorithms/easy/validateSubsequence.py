# whether the array2 is valid subsequence of array1
# O(n)time | 0(1) space
def validateSubsequence(array, sequence):
    seqIdx = 0
    for value in array:
        if seqIdx == len(sequence):
            break
        if value == sequence[seqIdx]:
            seqIdx += 1
    return seqIdx == len(sequence)


print(validateSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))