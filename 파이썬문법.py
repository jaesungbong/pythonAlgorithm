from collections import Counter
from itertools import product
from itertools import combinations_with_replacement

# 최빈값 구하기
a = [1,2,3,4,1,1,1]
b = Counter(a)
# 최빈값의 값 키 1
print(b.most_common(4)[0][0])
# 최빈값의 값 값 4번 등장
print(b.most_common(4)[0][1])


a = [1, 2, 3]
# 중복을 허용한 순열
c = list(product(a, repeat=2))
print(c)
# 중복을 허용한 조합
d = list(combinations_with_replacement(a, 2))
print(d)

#알파벳인지 숫자인지 확인
a = "K"
print(a.isalpha())

