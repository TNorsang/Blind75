# N-th Tribonacci Number

This is a remix of Fibonacci Problem.

Differences are it needs to calculate using 3 sequences rather than 2.

At first I did the normal way, without memoization:

```
if n == 0:
    return 0
if n == 1 or n == 2:
    return 1
return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
```

The issue with this solution is when it the n exceeds certain amount and it will take too long to compute. approximately

With Memoization:

```
def tribonacci(self, n: int) -> int:
    memo = {}

    def dp_tribonacci(n):
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        if n in memo:
            return memo[n]
        memo[n] = dp_tribonacci(n-1) + dp_tribonacci(n-2) + dp_tribonacci(n-3)
        return memo[n]
    return dp_tribonacci(n)
```

## Without Memoization

    Time Complexity: O(3^n) Each steps are calculated again without storing.
    Space Complexity: O(n) Memoization and recursion stack space

## With Memoization

    Time Complexity: O(n) Iterate through input only once
    Space Complexity: O(n) Memoization and recursion stack space
