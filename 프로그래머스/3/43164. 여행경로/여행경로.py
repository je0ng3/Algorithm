from collections import deque

def solution(tickets):
    answer = []
    
    tickets.sort()
    used = [False]*len(tickets)
    path = ["ICN"]
    
    def dfs(cur):
        if len(path)==len(tickets)+1:
            answer.extend(path)
            return True
        for i in range(len(tickets)):
            if not used[i] and tickets[i][0]==cur:
                used[i] = True
                path.append(tickets[i][1])
                
                if dfs(tickets[i][1]):
                    return True
                path.pop()
                used[i] = False
        return False
    
    dfs("ICN")
    return answer