def solution(schedules, timelogs, startday):
    answer = 0
    n = len(schedules)
    for i in range(n):
        if check(mm(schedules[i]), list(map(mm,timelogs[i])), startday):
            answer += 1
    return answer

def mm(time):
    h = time//100
    m = time%100
    return h*60+m

def check(schedule, timelog, startday):
    for i in range(7):
        if (startday+i)%7>5 or (startday+i)%7==0:
            continue
        if timelog[i]-10>schedule:
            return 0
    return 1