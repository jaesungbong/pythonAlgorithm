from collections import deque

def bfs():
    queue = deque()
    queue.append((0, 0))

    while queue:
        now = queue.popleft()
        x, y = now[0], now[1]

        for dx, dy in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            mx, my = x + dx, y + dy
            if 0 <= mx < n and 0 <= my < m and miro[mx][my] == 1:
                if (mx, my) != (0, 0):
                    miro[mx][my] = miro[x][y] + 1
                    queue.append((mx, my))

n, m = map(int, input().split())
miro = []
for i in range(n):
    miro.append(list(map(int, input())))

bfs()

for i in miro:
    print(i)