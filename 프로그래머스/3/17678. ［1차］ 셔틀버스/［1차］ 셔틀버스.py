from collections import deque

def solution(n, t, m, timetable):
    answer = 0
    timetable = deque(sorted([time_to_min(t) for t in timetable]))
    cur = time_to_min('09:00') # 시작 시간
    for _ in range(n):
        for _ in range(m):
            if timetable and timetable[0]<=cur: 
                answer = timetable.popleft()-1
            else:
                answer = cur
        cur += t
    answer = min_to_time(answer)
    return answer
    

def time_to_min(time: str) -> int:
    h, m = map(int, time.split(':'))
    return h*60+m

def min_to_time(min: int) -> str:
    h, m = min//60, min%60
    return str(h).zfill(2)+':'+str(m).zfill(2)