def solution(cap, n, deliveries, pickups):
    answer = 0
    idps = [(i, d, p) for i, (d, p) in enumerate(zip(deliveries, pickups), 1) if d or p]
    delivery = pickup = 0
    while idps:
        i, d, p = idps.pop() # 멀리있는 집부터
        delivery += d
        pickup += p
        while delivery>0 or pickup>0:
            delivery -= cap
            pickup -= cap
            answer += i*2
    return answer