from collections import deque

def solution(places):
    answer = []
    for place in places:
        answer.append(check(list(map(list,place))))
    return answer

def check(place):
    dr = [0,0,1,-1]
    dc = [1,-1,0,0]
    def search(row, col):
        q = deque([(row, col, 0)])
        place[row][col]='-'
        while q:
            r, c, count = q.popleft()
            if place[r][c]=='P':
                return 1
            place[r][c]='-' # 방문
            if count==2:
                continue
            for i in range(4):
                nr, nc = r+dr[i], c+dc[i]
                if 0<=nr<5 and 0<=nc<5 and place[nr][nc]!='X':
                    q.append((nr, nc, count+1))
        return 0
    
    for row, p_ in enumerate(place):
        for col, p in enumerate(p_):
            if p=='P':
                if search(row, col):
                    return 0
    return 1
