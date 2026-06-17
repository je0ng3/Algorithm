def solution(numbers):
    answer = []
    stack = []
    for num in numbers[::-1]:
        if not stack:
            stack.append(num)
            answer.append(-1)
            continue
        is_big = stack.pop()
        while stack and is_big<=num:
            is_big = stack.pop()
        if is_big>num:
            stack.append(is_big)
            answer.append(is_big)
        else:
            answer.append(-1)
        stack.append(num)

    return answer[::-1]

## 2, 3, 3, 5
# [] -> -1, [5]
# 5>3 -> 5, [5,3]
# 3=3 ->[5]-> 3<5->5,[5,3]
# 2<3 -> 3