# D > A > B > C
from collections import deque

n = int(input())

way = ["A", "B", "C", "D"]
ways = [deque() for _ in range(4)]
left_way = [1, 2, 3, 0] # A일때 B, B일때 C, C일때 D, D일때 A
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
    for i in range(len(ways)):
        if ways[i] and min_time == ways[i][0]:
            # 왼쪽에 차량이 있다면 왼쪽과 그 뒤 이어 지는 차량은 모두 +1 해준다.
            if ways[left_way[i]] and ways[left_way[i]][0] == min_time:
                temp_time = min_time
                for j in range(len(ways[left_way[i]])):
                    if ways[left_way[i]][j] == temp_time:
                        ways[left_way[i]][j] += 1
                        temp_time += 1
                    else:
                        break
            result.append(ways[i].popleft())
            min_time += 1
    print("A:{}, B:{}, C:{}, D:{}".format(ways[0], ways[1], ways[2], ways[3]))
    print()
print(result)







