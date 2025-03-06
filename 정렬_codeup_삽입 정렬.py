# 오름차순 삽입 정렬은 '정렬된 데이터 셋에 뒤쪽에서 부터 원소를 하나씩 삽입하여 순서에 맞는 위치로 찾아가며 정렬하는 방식'이다.
# 이번 문제는 미리 작성된 코드를 보고 빈 칸에 들어갈 코드를 작성하는 것이다.
# 이 프로그램은 선택 정렬을 구현한 것이며, 실행 결과는 오름차순으로 정렬된다.
# 빈 칸에 들어갈 코드만 작성해서 제출하시오.

# 입력 예시
# 5
# 1
# 3
# 2
# 5
# 4
#
# 출력 예시
# 1
# 2
# 3
# 4
# 5

n = int(input())
arr = [0] * (n + 1)
for i in range(1, n + 1):
    arr[i] = int(input())

for i in range(2, n + 1):
    key = arr[i]
    for j in range(i, 1, -1):
        if arr[j] < arr[j - 1]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]

for i in range(1, n + 1):
    print(arr[i])
