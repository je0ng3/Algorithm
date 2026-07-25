def solution(n, info):
    answer = [-1]

    # 라이언
    lion = [0]*11 # 10~0
    max_diff = 0
    
    def dfs(lion, arrow, point):
        nonlocal answer, max_diff
        
        # 점수 계산
        if arrow==0 or point==11:
            lion[10]=arrow # 남은 화살이 있다면 사용
            a_s = l_s = 0
            for i, (a, l) in enumerate(zip(info, lion)):
                if a or l:
                    s = 10-i
                    if a<l:
                        l_s+=s
                    else:
                        a_s+=s
            if a_s<l_s:
                diff = l_s-a_s
                if max_diff <diff:
                    answer = lion[:]
                    max_diff = diff
                elif max_diff==diff and \
                    answer[::-1]<lion[::-1]:
                    answer = lion[:]
            lion[10]-=arrow # 백트래킹
            return 
        
        score = 10-point # 점수 인덱스
        # 현재 점수 포기
        dfs(lion, arrow, point+1) # 다음 과녁 
        # 현재 점수 획득
        if info[score]<arrow: 
            need = info[score]+1
            lion[score] = need
            arrow-= need
            dfs(lion, arrow, point+1)
            arrow+= need  # 백트래킹
            lion[score]-=need
    
    dfs(lion, n, 0)
    return answer