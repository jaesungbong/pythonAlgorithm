def delay_time(arr, primary_key):
    for i in range(len(arr)):
        if arr[i][1] == primary_key:
            arr[i][0] += 1
    return arr


def time_pass(arr, time):
    temp_list = [item[1] for item in arr if item[0] == min_time]
    for j in temp_list:
        if j == "A":
            if "D" in temp_list:
                delay_time(arr, "A")
            else:
                print(time)  # 지나가는 시간 출력
        elif j == "B":
            if "A" in temp_list:
                delay_time(arr, "B")
            else:
                print(time)  # 지나가는 시간 출력
        elif j == "C":
            if "B" in temp_list:
                delay_time(arr, "C")
            else:
                print(time)  # 지나가는 시간 출력
        elif j == "D":
            if "C" in temp_list:
                delay_time(arr, "D")
            else:
                print(time)  # 지나가는 시간 출력
    print(arr)


n = int(input())

min_time = 1000000001
max_time = -1
high_way = []

for i in range(n):
    time, way = input().split()
    high_way.append([int(time), way])
    max_time = max((int(time), max_time))
    min_time = min((int(time), min_time))

# D > A > B > C

while True:
    if min_time == max_time:
        break
    time_pass(high_way, min_time)
    min_time += 1
    max_time = max([itm[0] for itm in high_way])





