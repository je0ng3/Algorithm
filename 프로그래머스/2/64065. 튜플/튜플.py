def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split("},{")
    s.sort(key=len)
    for i in s:
        i = i.split(",")
        for x in i:
            if int(x) not in answer:
                answer.append(int(x))
                break
    return answer