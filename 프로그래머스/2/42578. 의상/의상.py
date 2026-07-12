def solution(clothes):
    answer = 1
    kinds = {}
    for name, kind in clothes:
        kinds[kind] = kinds.get(kind, 1) + 1 # 초기 1인 이유: 안입을수도 있으니까
    for v in kinds.values():
        answer *= v
    return answer-1  # 모든 종류를 다 착용하지 않는 경우 제거