n, k = map(int, input().split()) # 5, 5
arr = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

if n > 0:
    arr[1][1] = 1

if n > 1:
    arr[1][2] = 1
    arr[2][2] = 1

if n > 3:
    arr[2][3] = 1

    for i in range(3, n + 1):
        for j  in range(1, n + 1):
            arr[i][j] = arr[i - 2][j - 1] + arr[i - 1][j - 1]

for row in arr:
    print(row)
