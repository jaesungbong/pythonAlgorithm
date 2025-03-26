def stair_climb(n):
    if n == 1:
        return 1

    if n == 2:
        return 2

    return stair_climb(n - 1) + stair_climb(n - 2)

n = int(input()) #계단 목표

print(stair_climb(n))

