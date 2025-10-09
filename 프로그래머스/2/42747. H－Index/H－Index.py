def solution(citations):
    h = -1
    citations = sorted(citations)
    n = len(citations)
    for i in range(citations[-1]+1):
        idx = find_idx(citations, i)
        if idx==-1 or n-idx<i:
            break
        h = max(h, i)
    return h

def find_idx(citations, i):
    for idx, c in enumerate(citations):
        if i<=c:
            return idx
    return -1