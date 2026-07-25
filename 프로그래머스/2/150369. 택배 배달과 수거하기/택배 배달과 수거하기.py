def solution(cap, n, deliveries, pickups):
    answer = 0
    idps = [(i,d,p) for i, (d, p) in enumerate(zip(deliveries, pickups), 1)]
    deliver = 0
    pickup = 0
    for i, d, p in idps[::-1]:
        deliver += d
        pickup += p
        while deliver>0 or pickup>0:
            answer += i*2
            deliver -= cap
            pickup -= cap
    return answer