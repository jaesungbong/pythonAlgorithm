n = int(input())
list = []
for i in range(n):
    math_score, info_score = map(int, input().split())
    list.append((i+1, math_score, info_score))

list.sort(key=lambda itm:(itm[1], itm[2], -itm[0]), reverse=True)
for row in list:
    print(" ".join(map(str, row)))