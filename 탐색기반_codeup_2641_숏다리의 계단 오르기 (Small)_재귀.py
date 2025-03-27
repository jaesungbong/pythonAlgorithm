def count_ways(target, numbers):
    if target == 0:
        return 1  # 합이 0이 되는 경우는 1가지 (아무것도 선택하지 않음)
    if target < 0:
        return 0  # 합이 음수가 되는 경우는 0가지

    total_ways = 0
    for number in numbers:
        total_ways += count_ways(target - number, numbers)

    return total_ways


# 원소 리스트
numbers = [1, 2, 3]
target_sum = 5

# 경우의 수 계산
result = count_ways(target_sum, numbers)
print(result)