from itertools import combinations

def check(tuple):
    for i in range(0, len(tuple) - 1):
        if abs(tuple[i] - tuple[i + 1]) == 1:
            return False
    return True

n, k = map(int, input().split())

cases = [itm for itm in list(combinations([itm for itm in range(1, n + 1)], k)) if check(itm)]
print(len(cases))