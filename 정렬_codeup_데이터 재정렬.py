# 프로그래밍 문제를 풀다 보면 뒤죽박죽인 N개의 데이터를 숫자의 크기 순으로 0 ~ N-1까지의 숫자로 재정렬 해야되는 경우가 종종 있다.
# 예를 들어 N=5 이고, 50 23 54 24 123 이라는 데이터가 있다면, 2 0 3 1 4 가 된다.
# 데이터를 재정렬하는 프로그램을 작성하시오.

# 입력예시
# 5
# 50 23 54 24 123

# 출력예시
# 2 0 3 1 4

n = int(input())
arr = list(map(int, input().split()))
newArr = sorted(arr)
dic = {}
for i in range(n):
    dic[newArr[i]] = i

for row in arr:
    print(dic[row], end=" ")
