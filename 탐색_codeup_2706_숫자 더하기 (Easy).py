s = str(input())
arr = []
for i in range(len(s) - 1):
    arr.append(s[i:i + 2])

arr = list(map(int, arr))
arr.sort(reverse=True)

result = []

arr = list(map(str, arr))

print(arr)

for i in range(len(arr)):
    if s.index(arr[i]) > 0:
        print(arr[i])
        result.append(arr[i])
        s = str.replace(s, arr[i], "")
        print(s)



print(arr)