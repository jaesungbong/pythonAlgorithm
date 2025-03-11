def permute(s):
    result = []

    def backtrack(path, used):
        # 모든 문자 사용 시, 결과에 추가
        if len(path) == len(s):
            result.append(path)
            return

        for i in range(len(s)):
            if used[i]:  # 이미 사용된 문자인 경우 무시
                continue

            # 문자 사용
            used[i] = True
            backtrack(path + s[i], used)  # 다음 문자 추가
            used[i] = False  # 백트래킹: 문자 사용 해제

    used = [False] * len(s)  # 문자 사용 여부
    backtrack("", used)  # 빈 문자열로 시작
    return result


# 예시 사용
s = "abc"
permutations = permute(s)
print(permutations)