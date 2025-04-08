from collections import deque

q = deque()

q.append(5)
print(q)
q.append(2)
print(q)
q.append(3)
print(q)
q.append(7)
print(q)
q.popleft()
print(q)
q.append(1)
print(q)
q.append(4)
print(q)
q.popleft()
print(q)

print(q)
print(list(q)[::-1])