def solution(progresses, speeds):
    answer = []
    count = len(progresses)
    duration = []
    for i in range(count):
        if (100-progresses[i])%speeds[i]==0 :
            duration.append((100-progresses[i])//speeds[i])
        else:
            duration.append((100-progresses[i])//speeds[i] + 1)
    dev = 1
    _pass = 1
    prod = duration[0]
    for i in range(1,count):
        if _pass:
            duration = list(map(lambda x:x-prod, duration))
        if duration[i]<=0:
            dev+=1
            _pass = 0
        else:
            answer.append(dev)
            prod = duration[i]
            dev = 1
            _pass = 1
    answer.append(dev)
    return answer