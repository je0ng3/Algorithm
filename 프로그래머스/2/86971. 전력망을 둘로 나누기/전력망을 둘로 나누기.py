from collections import deque

def solution(n, wires):
    answer = float('inf')
    for i in range(len(wires)):
        new = wires[:]
        del new[i]
        answer = min(answer, check(n, new))
    return answer

def check(n, wires):
    m = [[] for _ in range(n+1)]
    for (a, b) in wires:
        m[a].append(b)
        m[b].append(a)
    
    stack = deque([1])
    visited = set()
    while stack:
        cur = stack.popleft()
        if cur in visited:
            continue
        visited.add(cur)
        for nxt in m[cur]:
            if nxt not in visited:
                stack.append(nxt)
    node = n-len(visited)
    node2 = n-node
    return abs(node-node2)