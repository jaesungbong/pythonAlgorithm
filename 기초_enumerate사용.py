# enumerate 사용. range와 다르게 idx, itm 둘다 접근 가능
my_list = [(1, "a"), (2, "b"), (3, "c"),(3, "d"), (4, "e")]
new_list = [itm for idx, itm in enumerate(my_list) if idx == 3]
print(new_list)

# iterable한 list를 iter함수를 통해 iterator객체로 생성 하여 첫번째 반환
print(next(iter(my_list)))

# 리스트에서 튜플의 첫번째 원소가 3 원소의 두번째 원소 알파벳을 출력.
print(next((item[1] for idx, item in enumerate(my_list) if 3 in item), None))
print(list(item[1] for idx, item in enumerate(my_list) if item[0] == 3))


print(3 in my_list)




