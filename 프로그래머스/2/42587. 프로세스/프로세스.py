def solution(priorities, location):
    answer = 0
    indexed = [(index, value) for index, value in enumerate(priorities)]
    while indexed:
        current = indexed.pop(0)
        if any(current[1] < other[1] for other in indexed):
            indexed.append(current)
        else:
            answer += 1
            if current[0] == location:
                return answer