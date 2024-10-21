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