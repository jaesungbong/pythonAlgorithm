# 입력
# 두 개의 자연수(a, b) 가 공백을 두고 입력된다.
# (1 <= a, b <= 2147483647)
#
# 출력
# 두 수의 최소공배수를 출력한다.
#
# 입력 예시
# 192 72
#
# 출력 예시
# 576

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a, b = map(int,input().split())

print((a * b) // gcd(a,b))