# How Sum

Write a function `howSum(targetSum, numbers) that takes in a targetSum and an array of
numbers as arguments.

The function should return an array containing any combination of elements that add up
to exactly the targetSum. If there is no combination that adds up to the targetSum, then
return null.

If there are multiple combinations possible, you may return any single one.

## Brute Force Approach

```
def howSum(targetSum, numbers):
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    for num in numbers:
        remainder = targetSum - num
        remainderResult = howSum(remainder,numbers)
        if remainderResult is not None:
            remainderResult.append(num)
            return remainderResult
    return None

print(howSum(7,[2,3]))
print(howSum(7,[5,3,4,7]))
```

## Memoization Method

```
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
```
