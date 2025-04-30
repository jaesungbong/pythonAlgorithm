def dfs(index, path):
    global max_path
    # 현재 경로가 가장 길다면 저장
    if len(path) > len(max_path):
        max_path = path[:]

    for next in range(index + 1, len(stones)):
        if stones[next] > stones[index]:
            path.append(stones[next])
            dfs(next, path)
            path.pop()  # 백트래킹

n = int(input())
stones = list(map(int, input().split()))

max_path = []

for i in range(n):
    dfs(i, [stones[i]])

print(len(max_path))
