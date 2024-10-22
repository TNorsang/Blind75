# Min Cost Climbing Stairs

The problem wants you to find the min cost of a path when climbing a stair case.

Each stair block has a cost value.

1: You can either start from index 0 = stair 1 or index 1 = stair 2.
2: From there you can jump 1 or 2 steps.
3: Return the min

As you can see, there are multi decisions to make when trying to solve this problem.
And each decision it is important to remember the cost it took to reach to that current index
based on the path.

## Brute Force Implementation First

Step 1: Find the recursive brute force:

- Visualize the problem as a tree
- Implement the tree using recursion
- Test it

```
def minCostClimbingStairs(cost):
    if len(cost) == 2:
        return min(cost[0],cost[1])

    # Helper function that takes two index values:
    def find_min_cost(i):
        # Base Case: if the len of index >= len(cost): return
        if i >= len(cost):
            return 0

        current_cost = cost[i]
        current_cost += min(find_min_cost(i+1), find_min_cost(i+2))
        return current_cost

    return min(find_min_cost(0), find_min_cost(1))
```

## Memoization Approach

Step 2: Implement Memoization:

- Add a memo object
- Add a new base case to return memo values
- Store return values into the memo

```
def minCostClimbingStairs(cost):
    memo = {}

    if len(cost) == 2:
        return min(cost[0],cost[1])

    # Helper function that takes two index values:
    def find_min_cost(i):
        # Base Case: if the len of index >= len(cost): return
        if i >= len(cost):
            return 0

        if i in memo:
            return memo[i]

        current_cost = cost[i]
        current_cost += min(find_min_cost(i+1), find_min_cost(i+2))
        memo[i] = current_cost
        return memo[i]

    return min(find_min_cost(0), find_min_cost(1))
```
