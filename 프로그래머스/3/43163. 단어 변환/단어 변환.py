from collections import deque

def solution(begin, target, words):
    answer = 0

    def is_one_diff(a, b):
        return sum(x!=y for x, y in zip(a,b))==1
    
    queue = deque([(begin, 0)])
    visited = set([begin])

    while queue:
        word, cnt = queue.popleft()

        if word == target:
            return cnt
        
        for w in words:
            if w not in visited and is_one_diff(word, w):
                visited.add(w)
                queue.append((w, cnt+1))
            
    return 0