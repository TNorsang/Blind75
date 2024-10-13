def fib(n,memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib(n-2,memo) + fib(n-1,memo)
    return memo[n]

# 3 -> 1+1 = 2
# 4 -> 2+1 = 3
# 5 -> 3+1 = 4

'''
           5
      3        4
    1   2    2   3
                1 2     
3 -> 2
4 -> 3
5 -> 5
6 -> 8
7 -> 13
8 -> 21
9 -> 34
10 -> 55
'''
print(fib(50))
