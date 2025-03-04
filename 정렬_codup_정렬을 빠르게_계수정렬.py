# N개의 입력 데이터가 주어지면 정렬해서 출력하시오.
#
# 입력 예시
# 5
# 2 6 4 8 6
#
# 출력 예시
# 2 4 6 6 8

n = int(input())
arr = list(map(int, input().split()))
cnt = [0] * 1001

for i in range(len(arr)):
    cnt[arr[i]] += 1

for i in range(len(cnt)):
    if cnt[i] > 0:
        for j in range(cnt[i]):
            print(i, end=" ")