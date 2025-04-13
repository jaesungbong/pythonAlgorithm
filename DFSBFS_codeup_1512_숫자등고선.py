from collections import deque

def bfs(arr, height, coor_x, coor_y):
    queue = deque()
    queue.append((coor_x, coor_y))

    arr[coor_x][coor_y] = height

    idx = 0

    while queue:
        coor = queue.popleft()
        # 상, 우, 하, 좌
        for mx, my in [[-1, 0],[0, 1],[1, 0],[0, -1]]:
            dx, dy = coor[0] + mx, coor[1] + my
            if 0 <= dx < len(arr) and 0 <= dy < len(arr):
                if arr[dx][dy] == 0:
                    arr[dx][dy] = arr[coor[0]][coor[1]] + 1
                    queue.append((dx, dy))

n = int(input())
x, y = map(int, input().split())


mountain = [[0 for _ in range(n)] for _ in range(n)]
bfs(mountain, 1, x - 1, y - 1)

for i in mountain:
    for j in i:
        print(j, end=" ")
    print()