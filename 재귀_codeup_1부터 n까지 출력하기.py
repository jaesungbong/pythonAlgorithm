# 입력
# 정수 n이 입력된다 (1 <= n <= 200)
#
# 출력
# 1부터 n까지 한 줄에 하나씩 출력한다.
#
# 입력 예시
# 10
#
# 출력 예시
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
def f(n):
    if n == 0:
        return
    f(n - 1)
    print(n)

n = int(input())
f(n)