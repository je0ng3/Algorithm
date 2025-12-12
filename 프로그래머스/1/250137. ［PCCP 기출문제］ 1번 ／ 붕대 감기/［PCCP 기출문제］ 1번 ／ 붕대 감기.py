def solution(bandage, health, attacks):
    answer = health
    (t, x, y) = bandage
    now = 0     # 현재 시간
    for (at, ax) in attacks:
        time = at-now-1  # 치료 시간
        now = at
        if time >= t:
            plus = time//t  # 추가 회복 횟수
            answer = min(health, answer+time*x+y*plus)
        else:
            answer = min(health, answer+time*x)
        answer -= ax
        if answer < 1:
            return -1
    return answer