def recur(n):
    if n == 1:
        return 1
    if n > 10000000:
        if n % 2 == 0:
            return recur(n // 2) + 1
        else:
            return recur( 3 * n + 1) + 1
    else:
        if arr[n]:
            return arr[n]
        else:
            if n % 2 == 0:
                arr[n] = recur(n // 2) + 1
            else:
                arr[n] = recur(3 * n + 1) + 1
            return arr[n]

start, end = map(int, input().split())

max_num = 0
max_val = float('-inf')

arr = [0] * 10000001
arr[1] = 1

for i in range(start, end + 1):
    if not arr[i]:
        recur(i)

    if max_val < arr[i]:
        max_val = arr[i]
        max_num = i

print(max_num, max_val)
