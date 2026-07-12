import heapq

def solution(n, k, enemy):
    heap = [] # 최대힙
    for i, e in enumerate(enemy):
        heapq.heappush(heap, -e)
        n-=e
        if n>=0:
            continue
        if k:
            n -= heapq.heappop(heap)
            k -=1
        else:
            return i
    if n<0:
        return 0
    else:
        return len(enemy)
# n명으로 연속되는 적의 공격을 순서대로 막기
# 처음 병사 n
# 매 라운드마다의 적 수 enemy[i]
# 병사 한명당 적 한명

# 스킬 무적권: 한 라운드 병사 소모 없음. 사용제한 k번