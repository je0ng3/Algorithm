def solution(dirs):
    answer = 0
    key = {
        'U': (-1,0), 'D': (1, 0),
        'R':(0,1), 'L': (0, -1)
    }
    
    went = set()
    new_line = tuple(sorted([(0,0), key[dirs[0]]]))
    now = key[dirs[0]]
    went.add(new_line) # 간선 체크
    for dir in dirs[1:]:
        new = tuple(x+y for x, y in zip(now, key[dir]))
        if -5<=new[0]<=5 and -5<=new[1]<=5: # 범위 벗어나는 이동은 무시
            new_line = tuple(sorted([now, new]))
            went.add(new_line)
            now = new
    
    answer = len(went)
    return answer

