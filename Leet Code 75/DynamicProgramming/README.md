# Dynamic Programming:

Fibancci Problem

Step 1: Find the recursive brute force:

- Visualize the problem as a tree
- Implement the tree using recursion
- Test it

```
def fib(n):
    if n <= 2:
        return 1
    return fib(n-2) + fib(n-1)
```

Step 2: Implement Memoization:

- Add a memo object
- Add a new base case to return memo values
- Store return values into the memo

```
def fib(n,memo=None):
    if memo is None:
        memo = {}
    if n <= 2:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = fib(n-2) + fib(n-1)
```

## OR

```
def fib(n,memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib(n-2,memo) + fib(n-1,memo)
    return memo[n]
```

With passing memo as None initially, each call starts with a frest state if no memo dictionary is passed, avoiding
side effects from previous calls.
With passing memo as dictionary, it provides simplicity and dictionary persists between different calls to the function during the same program execution.
