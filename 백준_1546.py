def trans_score(origin_score):
    result = (origin_score / max_val) * 100
    return result

n = int(input())
scores = list(map(int, input().split()))
max_val = max(scores)
new_scores = [trans_score(i) for i in scores]

print(sum(new_scores) / n)
