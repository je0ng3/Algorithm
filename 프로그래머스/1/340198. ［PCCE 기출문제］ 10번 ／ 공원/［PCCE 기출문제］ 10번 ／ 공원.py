def solution(mats, park):
    answer = -1
    h, w = len(park), len(park[0])
    mats.sort(reverse=True)
    
    def maxi(x, y):
        for mat in mats:
            check = 0   
            if not (x+mat<=h and y+mat<=w):
                continue
            for row in park[x:x+mat]:
                if any(ym!="-1" for ym in row[y:y+mat]):
                    check = 1
                    break
            if check:
                continue
            mats.remove(mat)
            return mat
        return -1
    
    for i in range(h):
        for j in range(w):
            if park[i][j] != "-1":
                continue
            answer = max(answer, maxi(i, j))
    return answer