def make_m(time):
    h, m = time.split(":")
    return int(h)*60+int(m)

def solution(fees, records):
    parking = {}
    total = {}
    for record in records:
        time, car_num, in_out = record.split()
        if in_out=='IN':
            parking[car_num] = make_m(time)
        else: # OUT
            total[car_num] = total.get(car_num, 0) + make_m(time)-parking.pop(car_num)
    
    END = make_m("23:59")
    for car_num, time in parking.items():
        total[car_num] = total.get(car_num, 0)+END-time
            
    answer = []
    for _, time in sorted(total.items()):
        fee = fees[1]
        time-=fees[0]
        if time>0:
            fee += (time+fees[2]-1)//fees[2]*fees[3]
        answer.append(fee)
    return answer


# fees: 기본시간(분) 기본요금(원) 단위시간(분) 단위요금(원)
# record: 시각(시:분) 차량번호 내역(IN/OUT)

# 출차된 내역이 없으면 23:59에 출차된 것
# 초과 시간은 올림하여 청구
# 차량 번호가 작은 자동차 순으로 주차 요금 리턴

# 하루동안의 기록만 존재, 모두 당일 출차함
# 같은 차량번호 없음