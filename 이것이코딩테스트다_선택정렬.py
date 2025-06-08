li = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(li)):
    min_val = min(li[i:])
    min_val_idx = li.index(min_val)
    li[i], li[min_val_idx] = min_val, li[i]

print(li)