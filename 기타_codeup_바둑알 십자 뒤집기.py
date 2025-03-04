board = [list(map(int, input().split())) for _ in range(19)]
# 뒤집기 횟수
n = int(input())
info = [[0] * 2 for _ in range(n)]
for i in range(n):
    info[i] = list(map(int, input().split()))

for i in range(n):
    x = info[i][0] - 1
    y = info[i][1] - 1
    # 세로 줄 모두 바꾸기
    for j in range(19):
        if board[j][y] == 0 and j != x:
            board[j][y] = 1
        elif board[j][y] == 1 and j != x:
            board[j][y] = 0
    # 가로 줄 모두 바꾸기
    for k in range(19):
        if board[x][k] == 0 and k != y:
            board[x][k] = 1
        elif board[x][k] == 1 and k != y:
            board[x][k] = 0

for i in range(len(board)):
    print(" ".join(map(str, board[i])))