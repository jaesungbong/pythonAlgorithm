def stair_climb(arr, n):
    if n == 1:
        arr[1] = 1
    elif n == 2:
        arr[2] = 2
    elif n == 3:
        arr[3] = 4

    arr[n] = arr[n - 2] + arr[n - 1]


n = int(input()) #계단 목표
arr = [0] * (n + 1) #계단 오르기 경우의 수
arr = [0] * (n + 1) #계단 오르기 경우의 수
#print(stair_climb(arr, n))

