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
    for i in range(len(way)):
        if direction == way[i]:
            ways[i].append(int(time))

print(ways)

result = []

while ways[0] or ways[1] or ways[2] or ways[3]:
    delay_list = []

    for i in range(len(ways)):
        if ways[i] and min_time == ways[i][0]:
            # 오른쪽에 차량이 있다면 자신과 그 바로 뒤 이어 지는 차량은 모두 +1 해준다.
            if ways[right_way[i]] and ways[right_way[i]][0] == min_time:
                delay_list.append([i, 0])

    for item in delay_list:
        temp_time = min_time
        time = item[1]
        for j in range(len(ways[item[0]])):
            if ways[item[0]][j] == temp_time:
                ways[item[0]][j] += 1
                temp_time += 1
            else:
                break

    for i in range(len(ways)):
        if ways[i] and min_time == ways[i][0]:
            result.append(ways[i].popleft())

    min_time += 1
    print("A:{}, B:{}, C:{}, D:{}".format(ways[0], ways[1], ways[2], ways[3]))
    print()

print(result)






