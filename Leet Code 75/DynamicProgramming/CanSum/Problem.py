def canSum(targetSum, numbers, memo={}):
    if targetSum in memo:
        return memo[targetSum]
    elif targetSum == 0:
        return True
    elif targetSum < 0:
        return False
    
    for num in numbers:
        remainder = targetSum - num
        if canSum(remainder,numbers,memo) == True:
            memo[targetSum] = True
            return True
    memo[targetSum] = False
    return False

print(canSum(300, [14,7]))
