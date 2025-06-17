case = int(input())
for _ in range(case):
    n = int(input())
    scores = list(map(int,input().split()))
    avg = sum(scores) / len(scores)
    ratio = round(len([i for i in scores if i > avg]) / n, 3)
    print(f"{ratio}%")