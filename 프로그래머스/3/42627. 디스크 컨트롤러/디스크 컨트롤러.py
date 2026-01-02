import heapq

def solution(jobs):
    answer = 0
    n = len(jobs) # 작업 개수
    disk = [] # 디스크 컨트롤러
    now = 0 # 현재 시간
    jobs.sort() # 시작 시간 기준 정렬
    i = 0 # job 번호
    while i<n or disk:
        while i<n and jobs[i][0] <= now: # now 이내 작업 모두 디스크에 저장
            s, l = jobs[i]
            heapq.heappush(disk, (l, s))
            i += 1
        if disk:
            l, s = heapq.heappop(disk)
            now += l
            answer += now-s
        else:
            now = jobs[i][0]
    return answer//n