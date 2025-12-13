def solution(players, m, k):
    answer = 0
    server = [0 for _ in range(len(players))]
    for i, player in enumerate(players):
        if player < m:
            continue
        more = max(0, player//m - server[i])
        answer += more
        for j in range(i, i+k):
            if j==len(players):
                break
            server[j] += more
    return answer

        