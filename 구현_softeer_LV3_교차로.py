def delay_time(high_way, primary_key, time):
    for i in range(len(high_way)):
        if high_way[i][1] == primary_key:
            if high_way[i][0] == time:
                high_way[i][0] += 1
                time += 1
            else:
                break
    return high_way

n = int(input())

min_time = 1000000001
high_way = []

for i in range(n):
    time, way = input().split()
    high_way.append([int(time), way])
    min_time = min((int(time), min_time))

# D > A > B > C
count = 0

while count != n:
    temp_list = [item[1] for item in high_way if item[0] == min_time]
    if "A" in temp_list and "B" in temp_list and "C" in temp_list and "D" in temp_list:
        high_way[high_way.index([min_time, "A"])][0] = -1
        high_way[high_way.index([min_time, "B"])][0] = -1
        high_way[high_way.index([min_time, "C"])][0] = -1
        high_way[high_way.index([min_time, "D"])][0] = -1
        count += 4
    else:
        for j in temp_list:
            if j == "A":
                if "D" in temp_list:
                    delay_time(high_way, "A", min_time)
                else:
                    count += 1
            elif j == "B":
                if "A" in temp_list:
                    delay_time(high_way, "B", min_time)
                else:
                    count += 1
            elif j == "C":
                if "B" in temp_list:
                    delay_time(high_way, "C", min_time)
                else:
                    count += 1
            elif j == "D":
                if "C" in temp_list:
                    delay_time(high_way, "D", min_time)
                else:
                    count += 1
    min_time += 1

for i in high_way:
    print(i[0])


