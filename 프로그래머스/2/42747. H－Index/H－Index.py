def solution(citations):
    n = len(citations)
    sorted_c = sorted(citations)
    for i, citation in enumerate(sorted_c):
        h = n-i
        if citation>=h:
            return h
    return 0

# h번 이상 인용된 논문이 h편 이상인 h의 최댓값

