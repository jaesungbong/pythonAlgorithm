def binary_search(start, end):
    if start > end:
        return None
    mid = (end + start) // 2
    if array[mid] == target:
        return mid
    if array[mid] > target:
        return binary_search(start, mid - 1)
    elif array[mid] < target:
        return binary_search(mid + 1, end)

n, target = 10, 7
array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

print(binary_search(0, n - 1))