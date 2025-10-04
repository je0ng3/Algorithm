## 누적 주차 시간에 따라 요금을 일괄로 정산..!!

def solution(fees, records):
    car_in = {}
    result = {}
    for record in records:
        time, car, in_out = record.split(' ')
        if in_out == "IN":
            car_in[car] = time2minute(time)
            if car not in result:
                result[car] = 0
        else: 
            result[car] += time2minute(time) - car_in[car]
            del car_in[car]
    
    for car, time in car_in.items():
        result[car] += time2minute("23:59") - car_in[car]
    
    return [rate(result[car],fees) for car in sorted(result.keys())]

# 시각 -> 분
def time2minute(time):
    h,m = map(int, time.split(':'))
    return h*60+m

# 시간에 따른 가격
def rate(minute, fees):
    base_time, base_fee, unit_time, unit_fee = fees
    if minute<=base_time:
        return base_fee
    over = minute-base_time
    over_fee = over//unit_time*unit_fee
    if over%unit_time>0:
        over_fee += unit_fee
    return base_fee + over_fee
