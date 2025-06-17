arr = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

arr_list = [0 for _ in range(max(arr) + 1)]

for i in arr:
    arr_list[i] += 1

for i in range(len(arr_list)):
    for j in range(arr_list[i]):
        print(i, end="")