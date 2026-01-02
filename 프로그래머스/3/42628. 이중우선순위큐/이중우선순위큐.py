import heapq

def solution(operations):
    answer = []
    q = []
    for operation in operations:
        oper, val = operation.split(" ")
        if oper == "I":
            heapq.heappush(q, int(val))
        elif q:
            if val == "1":
                q = sorted(q)[:-1]
            else:
                heapq.heappop(q)
    if q:
        answer = [max(q), heapq.heappop(q)]
    else:
        answer = [0,0]
    return answer