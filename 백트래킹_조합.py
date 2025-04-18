def combinations(arr, r):
    result = []

    def backtrack(start, path):
        # 조합의 길이가 r에 도달하면 결과에 추가
        if len(path) == r:
            result.append(path)
            return

        for i in range(start, len(arr)):
            # 현재 요소를 선택하고 다음 요소로 이동
            backtrack(i + 1, path + [arr[i]])

    backtrack(0, [])
    return result


# 예시 사용
arr = [1, 2, 3, 4]
r = 3
print(combinations(arr, r))