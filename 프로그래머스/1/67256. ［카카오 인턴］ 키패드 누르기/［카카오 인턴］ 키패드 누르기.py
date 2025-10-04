def solution(numbers, hand):
    answer = ''
    hand = 'L' if hand == 'left' else 'R'
    location_l, location_r = '*', '#'
    for num in numbers:
        if num in [1, 4, 7]: # 왼손 구역
            answer += 'L'
        elif num in [3, 6, 9]: # 오른손 구역
            answer += 'R'
        else:
            length_l = length(location_l, num)
            length_r = length(location_r, num)
            if length_l < length_r:
                answer += 'L'
            elif length_l == length_r:
                answer += hand
            else:
                answer += 'R'
        if answer[-1]=='L':
            location_l = num
        else:
            location_r = num
    return answer

# 특정 키패드에서 다른 키패드로 옮기는 데 드는 거리
def length(start, end):
    area = [[1,2,3],[4,5,6],[7,8,9],['*',0, '#']]
    idx_s = idx_e = 0
    for idx, a in enumerate(area):
        if start in a:
            idx_s = idx
            break
    for idx, a in enumerate(area):
        if end in a:
            idx_e = idx
            break
    result = abs(idx_s-idx_e)
    if start in [2,5,8,0]:
        result -=1
    return result
            