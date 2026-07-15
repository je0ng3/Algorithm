N = int(input())
scores = [list(map(int, input().split())) for _ in range(3)]

# Please write your code here.
def get_rank(score):
    sorted_s = sorted(score, reverse=True)
    rank = {}
    for i, s in enumerate(sorted_s):
        if s not in rank:
            rank[s] = i+1
    return [rank[s] for s in score]

for score in scores:
    ranks = get_rank(score)
    print(*ranks, sep=' ')
final_score = [sum(col) for col in zip(*scores)]
ranks = get_rank(final_score)
print(*ranks, sep=' ')

# 각 대회별(3개) 등수 및 최종 등수
# 동점 -> 1, 2, 2, 4 : 내 등수 = 나보다 점수가 큰 사람의 수 +1
# 최종 등수: 세 대회 점수 합 기준
