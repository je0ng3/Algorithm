import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville)>=1:
        a = heapq.heappop(scoville)
        if a>=K:
            break
        if len(scoville)>=1:
            b = heapq.heappop(scoville)
        else:
            return -1
        c = a + (b*2)
        heapq.heappush(scoville, c)
        answer+=1
    return answer