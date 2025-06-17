def binary_search(start, end):
    if start > end:
        return None

    result = 0
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for i in array:
            if i > mid:
                total += (i - mid)

        if total < m:
            end = mid - 1
        else:
            result = mid
            start = mid + 1

    return result

n, m = 4, 6
array = [19, 15, 10, 17]

print(binary_search(0, max(array)))

