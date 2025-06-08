def find_path(x, y):
    def dfs(coor_x, coor_y, path):
        temp_path.append((coor_x, coor_y))
        ice_board[coor_x][coor_y] = 1

        for dx, dy in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            mx, my = coor_x + dx, coor_y + dy
            if 0 <= mx < n and 0 <= my < m and ice_board[mx][my] == 0:
                dfs(mx, my, path)

    temp_path = []
    if ice_board[x][y] == 0:
        dfs(x, y, temp_path)

    return temp_path

n, m = map(int, input().split())

ice_board = []
for i in range(n):
    ice_board.append(list(map(int, input())))

ice_creams = []

for i in range(n):
    for j in range(m):
        temp_list = find_path(i, j)
        if len(temp_list) != 0:
            ice_creams.append(temp_list)

print(ice_creams)
print(len(ice_creams))

