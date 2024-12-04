def solution(dartResult):
    answer = 0
    score = [0]
    dartResult = dartResult.replace("10", "x")
    for r in list(dartResult):
        if r.isdigit():
            score.append(int(r))
        elif r == 'x':
            score.append(10)
        elif r == 'D':
            score[-1] = score[-1]**2
        elif r == 'T':
            score[-1] = score[-1]**3
        elif r == '*':
            score[-2] = score[-2]*2
            score[-1] = score[-1]*2
        elif r == '#':
            score[-1] = score[-1]*(-1)
    answer = sum(score)
    return answer