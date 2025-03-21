# 수열 속에 숨어 있는 보물들을 찾아보자. n개의 자연수로 이루어진 수열이 있다.
# 이 수열들 중 연속된 1개 이상의 원소들의 합이 정확히 k가 되면 이 구간은 보물구간이라고 한다.
# 주어진 n개의 자연수 중에서 보물 구간이 몇 개 있는지 구하는 프로그램을 작성하시오.
# 입력첫 번째 줄에 자연수 n과 k가 공백으로 구분되어 입력된다.
# 두 번째 줄에 n개의 각 원소가 공백으로 구분되어 입력된다.
# [입력값의 정의역]5<=n<=100,000각 원소는 1,000이하의 자연수출력보물 구간의 수를 출력한다.

# 입력 예시
# 5 15
# 1 2 3 4 5

# 출력 예시
# 1

def findBomul(nums, s):
    result = []

    def backtrack(start, path):
        print("start: {}, len(path):{}".format(start, len(path)))
        len(path)

        if sum(path) == s:
            result.append(path)
            return

        for i in range(start, len(nums)):
            backtrack(i + 1, path + [nums[i]])

    path = []
    backtrack(0, path)

    return result


n, s = map(int, input().split())
nums = list(map(int, input().split()))

print(findBomul(nums, s))