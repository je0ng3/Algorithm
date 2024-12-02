def solution(code):
    answer = ''
    mode = True
    a=[]
    b=[]
    for i, j in enumerate (list(code)):
        if j == "1":
            if mode:
                mode = False
            else:
                mode = True
        else:
            if (i%2==0 and mode) or (i%2!=0 and not mode):
                answer+= j
    if answer =='':
        return "EMPTY"
    return answer