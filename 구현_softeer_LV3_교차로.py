# D > A > B > C
from collections import deque

n = int(input())

way = ["A", "B", "C", "D"]
ways = [deque() for _ in range(4)]
right_way = [3, 0, 1, 2]
min_time = 1000000001

for i in range(n):
    time, direction = input().split()
    min_time = min(min_time, int(time))
    for j in range(len(way)):
        if direction == way[j]:
            ways[j].append([int(time), i + 1]) # [시간, 차량 번호]

result = []

while ways[0] or ways[1] or ways[2] or ways[3]:
    delay_list = []

    for i in range(len(ways)):
        if ways[i] and min_time == ways[i][0][0]:
            # 오른쪽에 차량이 있다면 자신과 그 바로 뒤 이어 지는 차량은 모두 +1 해준다.
            if ways[right_way[i]] and ways[right_way[i]][0][0] == min_time:
                delay_list.append(i)

    if len(delay_list) == 4:
        for i in range(4):
            result.append([-1, ways[i][0][1]])
        break

    for itm in delay_list:
        temp_time = min_time
        for j in range(len(ways[itm])):
            if ways[itm][j][0] == temp_time:
                ways[itm][j][0] += 1
                temp_time += 1
            else:
                break

    for i in range(len(ways)):
        if ways[i] and min_time == ways[i][0][0]:
            result.append(ways[i].popleft())

    min_time += 1

result.sort(key=lambda x:x[1])
for i in result:
    print(i[0])




