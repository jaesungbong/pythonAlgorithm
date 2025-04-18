def dfs(path, depth = 0):
    if path[-1] == check_points[depth]:
        depth += 1
        if len(check_points) == depth:
            result.append(path)
            return

    for mx, my in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        dx, dy = mx + path[-1][0], my + path[-1][1]

        if 0 <= dx < len(matrix) and 0 <= dy < len(matrix) and (dx, dy) not in path and matrix[dx][dy] != 1:
            dfs(path + [(dx, dy)], depth)


n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
check_points = [tuple(map(lambda x:x - 1,list(map(int, input().split())))) for _ in range(m)]
result = []
dfs([check_points[0]], 0)
print(len(result))