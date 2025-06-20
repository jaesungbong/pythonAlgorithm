n = [1, 3, 1, 5, 7, 6]

dp = [0] * len(n)

dp[0] = 1
dp[1] = max(n[0], n[1])
for i in range(2, len(n)):
    dp[i] = max(dp[i - 1], dp[i - 2] + n[i])

print(dp)