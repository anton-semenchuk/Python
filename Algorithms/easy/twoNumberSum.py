# find the pair of numbers that corresponds to the target
# O(n) time | O(1) space
def twoNumberSum(nums, target):
    nums.sort()
    leftIdx = 0
    rightIdx = len(nums) - 1
    while leftIdx < rightIdx:
        result = nums[leftIdx] + nums[rightIdx]
        if result == target:
            return [nums[leftIdx], nums[rightIdx]]
        elif result < target:
            leftIdx += 1
        else:
            rightIdx -= 1
    return False


# O(n) time | O(n) space
def twoNumberSum2(array, target):
    nums = {}
    for num in array:
        if target - num in nums:
            return [num, target - num]
        else:
            nums[num] = True
    return nums


print(twoNumberSum2([3, 5, -4, 8, 11, 1, -1, 6], 111))