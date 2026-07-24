from collections import deque

def solution(n, info):
    answer = [-1] 
        
    # 라이언
    # 가장 큰 점수 차이, 낮은 점수 많이 맞춘 것 우선
    lion = [0]*11 # 0~10
    max_diff = 0
    
    def dfs(idx, arrow):
        nonlocal answer, max_diff
        
        if idx==11:
            # 남은 화살은 0점
            if arrow>0:
                lion[10]=arrow
            # 점수 계산
            a_score = l_score = 0
            for i in range(11):
                score = 10-i
                if info[i]==0 and lion[i]==0:
                    continue
                if lion[i]>info[i]:
                    l_score += score
                else:
                    a_score += score
            diff = l_score - a_score
            if max_diff < diff:
                max_diff = diff
                answer = lion[:]
            elif diff>0 and max_diff == diff:
                if lion[::-1]>answer[::-1]:
                    answer = lion[:]
            
            if arrow>0:
                lion[10]-=arrow # 백트래킹
            return 
        
        # 과녁 안맞춤
        dfs(idx+1, arrow)
        # 과녁 맞춤
        need = info[idx]+1
        if arrow>=need:
            lion[idx] = need
            dfs(idx+1, arrow-need)
            lion[idx] = 0 # 백트래킹
        
    dfs(0, n)
    return answer
        
        
        