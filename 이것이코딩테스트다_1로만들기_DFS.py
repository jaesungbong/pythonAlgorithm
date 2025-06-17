def dfs(num, cnt=0):
    print(f"num:{num}, cnt:{cnt}")
    if num == 1:
        global total_cnt
        total_cnt = min(total_cnt, cnt)
        return

    if num % 5 == 0:
        dfs(num // 5, cnt + 1)
    if num % 3 == 0:
        dfs(num // 3, cnt + 1)
    if num % 2 == 0:
        dfs(num // 2, cnt + 1)

    dfs(num - 1, cnt + 1)


n = 26
total_cnt = float('inf')
dfs(n)
print(total_cnt)