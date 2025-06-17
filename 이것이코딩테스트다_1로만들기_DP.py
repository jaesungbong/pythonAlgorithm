def dp(num, memo):
    if memo[num] or num == 1 or num == 2:
        return memo[num]

    if num % 5 == 0:
        memo[num] = min(dp(num, memo), )

n = 26

memo = [0 for i in range(n + 1)]

memo[2] = 1
memo[3] = 1
memo[5] = 1

dp(n, memo)