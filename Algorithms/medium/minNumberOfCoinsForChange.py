# O(n) time | O(1) space
def minNumberOfCoinsForChange(n, denoms):
    result = 0
    for denom in reversed(denoms):
        if denom > n:
            continue
        result += int(n / denom)
        remainder = n % denom
        if remainder > 0:
            n = remainder
        elif remainder == 0:
            return result
    return result


# O(nd) time | O(n) space - where d is the number of denominations
def minNumberOfCoinsForChange2(n, denoms):
    ways = [0 for _ in range(n + 1)]
    for denom in denoms:
        for amount in range(1, n + 1):
            if denom <= amount:
                ways[amount] = 1 + ways[amount - denom]
    return ways[n]


money = 10  # $
coinDenominations = [1, 2, 4]
print(minNumberOfCoinsForChange(money, coinDenominations))

