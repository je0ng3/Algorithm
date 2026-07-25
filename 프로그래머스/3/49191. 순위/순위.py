from collections import defaultdict, deque

def solution(n, results):
    answer = 0
    
    win = defaultdict(list) # 날 이긴 선수
    lose = defaultdict(list) # 내가 이긴 선수
    for a, b in results:
        win[b].append(a)
        lose[a].append(b)
        
    def bfs(start, graph):
        visited = set()
        q = deque([start])
        while q:
            cur = q.popleft()
            for nxt in graph[cur]:
                if nxt not in visited:
                    visited.add(nxt)
                    q.append(nxt)
        return visited
        
    for i in range(1, n+1):
        wins = bfs(i, win)
        loses = bfs(i, lose)
        if len(wins)+len(loses)+1==n:
            answer+=1
    return answer
