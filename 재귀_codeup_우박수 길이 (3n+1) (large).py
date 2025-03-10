def recur(n):
    if n == 1:
        return 1

    k = 0

    if arr[n] != 0:
        return arr[n]

    if n % 2 == 0:
        k = n // 2
    else:
        k = 3 * n + 1
    arr[n] = recur(k) + 1

start, end = map(int, input().split())

max_num = 0
max_val = float('-inf')

arr = [0] * (end + 1)
arr[1] = 1

for i in range(start, end + 1):
    if arr[i] != 0:
        recur(i)
    print(i, arr[i])
    # k = recur(i)
    # print(i, k)
    # if k > max_val:
    #     max_val = k
    #     max_num = i

# print(max_num, max_val)