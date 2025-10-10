def solution(brown, yellow):
    for x, y in xy(yellow):
        if brown == outline(x, y):
            return [x+2, y+2]
    return -1

# 노란격자로 만들 수 있는 모든 네모의 가로,세로 길이 리스트
def xy(yellow):
    cases = []
    for i in range(1, int(yellow**0.5)+1):
        if yellow%i==0:
            cases.append((yellow//i, i))
    return cases

# 테두리
def outline(x, y):
    return (x+y)*2+4