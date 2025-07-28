def solution(prices):
    answer = [0] * len(prices)
    stack = []
    for i, price in enumerate(prices):
        while stack and price < prices[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)

    for s in stack:
        answer[s] = len(prices) - s - 1
        
    return answer
        