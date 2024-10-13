def howSum(targetSum, numbers, memo={}):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    for num in numbers:
        remainder = targetSum - num
        remainderResult = howSum(remainder,numbers,memo)
        if remainderResult is not None:
            remainderResult.append(num)
            memo[targetSum] = remainderResult
            return memo[targetSum]
    memo[targetSum] = None
    return None

print(howSum(7,[2,3]))
print(howSum(7,[5,3,4,7]))
print(howSum(300,[7,14]))