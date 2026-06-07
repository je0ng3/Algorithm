def solution(n, words):
    temp = ''
    turn = 0 
    used = set()
    for i, word in enumerate(words):
        if i==0 or temp==word[0] and word not in used:
            used.add(word)
            temp = word[-1]
        else:
            return [i%n+1, i//n+1]
        
    return [0,0]