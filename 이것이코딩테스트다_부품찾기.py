def binary_search(target, start, end):
    if start > end:
        return False
    mid = (start + end) // 2
    if array_n[mid] == target:
        return True
    elif array_n[mid] > target:
        return binary_search(target, start, mid - 1)
    elif array_n[mid] < target:
        return binary_search(target, mid + 1, end)

n = 5
array_n = [8, 3, 7, 9, 2]
array_n.sort()
print(array_n)
m = 3
array_m = [5, 7, 9]

for i in array_m:
    print(f"i:{i}")
    if binary_search(i, 0, len(array_n) - 1):
        print("yes", end="")
    else:
        print("no", end="")
    print()