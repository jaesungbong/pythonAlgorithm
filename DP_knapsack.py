def knapsack(weights, values, W):
    n = len(weights)
    # DP 테이블 초기화
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # DP 테이블 채우기
    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i - 1] <= w:
                print("dp[{}][{}] = max(dp[{}][{}], dp[{}][{}] + values[{}])".format(i, w, i - 1, w, i - 1, w - weights[i - 1], i -1))
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
        print(dp[i])

    return dp[n][W]

# 예시 사용
weights = [1, 4, 3]  # 물건의 무게
values = [10, 15, 40]  # 물건의 가치
W = 6  # 배낭의 최대 용량

max_value = knapsack(weights, values, W)
print("최대 가치:", max_value)