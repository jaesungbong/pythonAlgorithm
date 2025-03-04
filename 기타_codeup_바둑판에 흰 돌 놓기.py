board = [[0 for _ in range(19)] for _ in range(19)]

for i in range(int(input())):
    x, y = map(int,input().split())
    board[x - 1][y - 1] = 1

for row in board:
    print(" ".join(map(str, row)))