from collections import defaultdict, deque

def solution(n, results):
    answer = 0
    # win[i]: i를 이긴 선수
    # lose[i]: i에게 진 선수
    win = defaultdict(list)
    lose = defaultdict(list)
    for a, b in results:
        win[b].append(a)
        lose[a].append(b)
    for i in range(1, n+1):
        know = [False]*n
        know[i-1] = True
        q = deque(win[i])
        while q:
            who = q.popleft()
            know[who-1] = True
            for w in win[who]:
                if not know[w-1]:
                    q.append(w)
        q = deque(lose[i])
        while q:
            who = q.popleft()
            know[who-1]=True
            for l in lose[who]:
                if not know[l-1]:
                    q.append(l)
        if all(know):
            answer += 1
    return answer
