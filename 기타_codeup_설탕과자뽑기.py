# 부모님과 함께 놀러간 영일이는
# 설탕과자(설탕을 녹여 물고기 등의 모양을 만든 것) 뽑기를 보게 되었다.
#
# 길이가 다른 몇 개의 막대를 바둑판과 같은 격자판에 놓는데,
#
# 막대에 있는 설탕과자 이름 아래에 있는 번호를 뽑으면 설탕과자를 가져가는 게임이었다.
# (잉어, 붕어, 용 등 여러 가지가 적혀있다.)
#
# 격자판의 세로(h), 가로(w), 막대의 개수(n), 각 막대의 길이(l),
# 막대를 놓는 방향(d:가로는 0, 세로는 1)과
# 막대를 놓는 막대의 가장 왼쪽 또는 위쪽의 위치(x, y)가 주어질 때,
#
# 격자판을 채운 막대의 모양을 출력하는 프로그램을 만들어보자.

# 세로 가로 입력
height, width = map(int, input().split())
n = int(input()) # 막대 개수
info = [[0] * 4 for _ in range(n)] #막대 정보
for i in range(len(info)):
    info[i] = list(map(int, input().split()))

board = [[0] * width for _ in range(height)]

for row in info:
    length = row[0]
    d = row[1]
    x = row[2] - 1 # 시작x
    y = row[3] - 1 # 시작y
    for _ in range(length):
        board[x][y] = 1
        if d == 0: # 오른쪽으로
            y += 1
        elif d == 1: # 아래로
            x += 1

for row in board:
    print(" ".join(map(str, row)))

