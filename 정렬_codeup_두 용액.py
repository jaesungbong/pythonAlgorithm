n = int(input())
array = list(map(int, input().split()))
array.sort()
start_pointer = 0
end_pointer = len(array) - 1
min_val = 2000000000
pair = (array[start_pointer], array[end_pointer])
while start_pointer < end_pointer:
    if min_val > abs(array[start_pointer] + array[end_pointer]):
        min_val = abs(array[start_pointer] + array[end_pointer])
        pair = (array[start_pointer], array[end_pointer])
    if array[start_pointer] + array[end_pointer] > 0:
        end_pointer -= 1
    else:
        start_pointer += 1

print(pair[0], pair[1])




