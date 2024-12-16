def solution(a, b, c, d):
    answer = 0
    e = [a,b,c,d]
    e.sort()
    if e.count(e[0])==4:
        answer= 1111*e[0]
        
    elif e.count(e[0])==3:
        answer=pow((10*e[0]+e[-1]),2)
    elif e.count(e[-1])==3:
        answer=pow((10*e[-1]+e[0]),2)
        
    elif e.count(e[0])==2 and e.count(e[-1])==2:
        answer=((e[1]+e[2])*abs(e[1]-e[2]))

    elif e[1]==e[2]:
        answer=(e[0]*e[-1])
    
    elif e.count(e[-1])==2:
        answer=(e[0]*e[1])
    elif e.count(e[0])==2:
        answer=(e[2]*e[3])
            
    else:
        answer=e[0]
    return answer