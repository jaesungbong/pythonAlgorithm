def count_ways(target, cnt):
    if cnt > 0:
        cnt = cnt - 1

    if target == 0:
        return 1  # 합이 0이 되는 경우는 1가지 (아무것도 선택하지 않음)
    if target < 0:
        return 0  # 합이 음수가 되는 경우는 0가지

    total_ways = 0

    total_ways += count_ways(target - 1, cnt)
    total_ways += count_ways(target - 2, cnt)
    if cnt == 0:
        total_ways += count_ways(target - 3, 3)
    return total_ways


# 원소 리스트
target_sum = int(input())

# 경우의 수 계산
result = count_ways(target_sum, 0)
print(result)