n, m = map(int, input().split())
moneys = [int(input()) for _ in range(n)]

dp = [10001] * (m + 1)

dp[0] = 0

for i in range(min(moneys), m + 1):
    temp_val = 10001
    for mon in moneys:
        temp_val = min(temp_val, dp[i - mon] + 1)
    dp[i] = temp_val

print(dp)