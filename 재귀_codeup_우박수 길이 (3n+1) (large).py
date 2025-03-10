def recur(n, cnt):
    cnt += 1
    if n == 1:
        return cnt
    k = 0
    if n % 2 != 0:
        k = 3 * n + 1
    else:
        k = n // 2
    return recur(k, cnt)

start, end = map(int, input().split())
#
# num = 0
# max = float('-inf')
#
# for i in range(start, end + 1):
#     cnt = 0
#     recur(i)