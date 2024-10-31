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