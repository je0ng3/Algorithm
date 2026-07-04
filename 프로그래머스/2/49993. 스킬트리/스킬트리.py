def solution(skill, skill_trees):
    answer = 0
    skill_idx = {s:i for i, s in enumerate(list(skill))}
    for st in skill_trees:
        temp = [s for s in st if s in skill]
        check = -1
        available = 1
        for t in temp:
            if skill_idx[t] != check+1:
                available = 0
                break
            check += 1
        if available:
            answer += 1
    return answer