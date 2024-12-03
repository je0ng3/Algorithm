def solution(N, stages):
    stay = [0 for _ in range(N+2)]
    for i in stages:
        stay[i-1]+=1
    fail = []
    for i, s in enumerate (stay[:-2]):
        if sum(stay[i:])==0:
            fail.append([i+1,0])
        else:
            fail.append([i+1, s/sum(stay[i:])])
    a = sorted(fail, key = lambda x:x[1], reverse = True)
    answer = [i[0] for i in a]
    return answer
