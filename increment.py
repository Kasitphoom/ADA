"""Double, Triple, and Increment"""
memo = {}
def increment(x):
    if x in memo:
        return memo[x]
    if x == 1:
        memo[1] = 0
        return memo[1]

    if x % 3 == 0:
        memo[x] = min(increment(x / 3), increment(x - 1)) + 1
        return memo[x]
    if x % 2 == 0:
        memo[x] = min(increment(x / 2), increment(x - 1)) + 1
        return memo[x]
    if x - 1 > 0:
        memo[x] = increment(x - 1) + 1
        return memo[x]

print(increment(int(input())))
