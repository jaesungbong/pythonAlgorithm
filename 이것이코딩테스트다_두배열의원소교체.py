from collections import Counter

# 최빈값 구하기
a = [1,2,3,4,1,1,1]
b = Counter(a)
# 최빈값의 값 키 1
print(b.most_common(1))