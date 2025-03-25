from itertools import combinations
#n번째 칸으로 이동
#k개 이하의 칸 사용

# 차이가 2 이하인 원소만 필터링
def dff(tuple):
    for i in range(0, len(tuple) - 1):
        if abs(tuple[i] - tuple[i + 1]) > 2:
            return False
    return True

n, k = map(int, input().split()) # 5, 5

nums = [i for i in range(n + 1)]
nums = [itm for itm in list(combinations(nums, k)) if itm[0] == 0 and itm[len(itm) - 1] == n]
nums = list(filter(dff, nums))

print(len(nums))