def solution(n, stations, w):
    answer = 0
    prev = 0 # 커버된 마지막 집 번호
    for station in stations:
        length = (station-w)-(prev+1) # prev+1 ~ station-w-1
        prev = station+w
        answer += (length+2*w)//(w*2+1)
    # 마지막 오른쪽 구간
    length = n-prev
    answer += (length+2*w)//(w*2+1)
    return answer

# n개의 아파트 (일렬), 일부 옥상 위 4g 기지국 
# -> 5g 기지국으로 변환, 범위 좁아짐 -> 5g 추가 설치 필요

# 기지국이 설치된 아파트 번호 stations (정렬됨)
# 전파 도달 거리 w
# -> station +- w까지 가능