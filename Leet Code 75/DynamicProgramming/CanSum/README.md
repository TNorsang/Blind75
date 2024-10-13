# Can Sum

Write a function `canSum(targetSum, numbers)` that takes in a targetSum and an array of numbers as arguments.

The function should return a boolean indicating whether or not it is possible to generate the targetSum using numbers from the array.

You may use an element of the array as many times as needed.

You may assume that all input numbers are nonnegative

Brute Force Method:

```
def canSum(targetSum, numbers):
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False

    for num in numbers:
        remainder = targetSum - num
        if canSum(remainder,numbers) == True:
            return True
    return False
```

Memoization Method:

```
def canSum(targetSum, numbers, memo={}):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False

    for num in numbers:
        remainder = targetSum - num
        if canSum(remainder,numbers,memo) == True:
            memo[targetSum] = True
            return True
    memo[targetSum] = False
    return False

print(canSum(300, [14,7]))


```
