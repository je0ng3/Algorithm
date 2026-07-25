def solution(word):
    answer = 0
    vowels = ['A', 'E', 'I', 'O', 'U']
    
    def dfs(cur):
        nonlocal answer
        if cur:
            answer += 1
            if cur == word:
                return True
        if len(cur)==5:
            return False
        for v in vowels:
            if dfs(cur+v):
                return True
        return False
    dfs("")
    return answer