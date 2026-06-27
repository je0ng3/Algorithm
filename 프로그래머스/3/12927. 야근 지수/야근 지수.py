import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0 
    
    heap = [-w for w in works]
    heapq.heapify(heap)
    
    for _ in range(n):
        x = -heapq.heappop(heap)
        x -= 1
        heapq.heappush(heap, -x)
    
    answer = sum(x*x for x in heap)
    return answer

# 평균을 작게 만들어야 함 
# -> 제일 큰 값을 1씩 제거
# -> 반복 : 최대 힙 사용
