# prime 또는 composite 중 하나를 출력하시오.
# 단, 함수형 문제이므로 함수 f()만 작성하시오.

# 입력
# int 형 자연수(n)가 입력된다.
# (2 <= n <= 1000)
#
# 입력 예시
# 997
#
# 출력
# 소수(prime)가 입력되면 prime, 합성수(composite)가 입력되면 composite 를 출력한다.
#
# 출력 예시
# prime

n = int(input())
half = n // 2
flag = "prime"
for i in range(2, half + 1):
    if n % i == 0:
        flag = "composite"
        break

print(flag)

