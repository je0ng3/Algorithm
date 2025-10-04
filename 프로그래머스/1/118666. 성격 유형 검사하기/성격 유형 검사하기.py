def solution(survey, choices):
    answer = ''
    score = {"R":0, "T":0, "C":0,"F":0, "J":0,"M":0, "A":0, "N":0}
    for s, c in zip(survey, choices):
        if c==4:
            continue
        elif c<4:
            score[s[0]]+=calculate(c)
        else:
            score[s[1]]+=calculate(c)
    answer += "R" if score["R"]>=score["T"] else "T"
    answer += "C" if score["C"]>=score["F"] else "F"
    answer += "J" if score["J"]>=score["M"] else "M"
    answer += "A" if score["A"]>=score["N"] else "N"
    return answer

def calculate(c):
    if c==1 or c==7:
        return 3
    if c==2 or c==6:
        return 2
    if c==3 or c==5:
        return 1