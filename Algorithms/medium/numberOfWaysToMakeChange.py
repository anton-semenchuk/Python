# 0(nd) time | 0(n) space - where d is the number of coin denominations
def numberOfWaysToMakeChange(n, denoms):
    ways = [0 for amount in range(n + 1)]
    ways[0] = 1
    for denom in denoms:
        for amount in range(1, n + 1):
            if denom <= amount:
                ways[amount] += ways[amount - denom]
    return ways


money = 20  # $
coinDenominations = [1, 5, 10, 25]
print(numberOfWaysToMakeChange(money, coinDenominations))
