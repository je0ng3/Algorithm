def solution(numbers):
    nums = set()
    visited = [False]*len(numbers)
    def dfs(cur):
        if cur:
            nums.add(int(cur))
        for i in range(len(numbers)):
            if not visited[i]:
                visited[i] = True
                dfs(cur+numbers[i])
                visited[i] = False
    dfs("")
    
    def is_prime(n):
        if n<2:
            return False
        for i in range(2, int(n**0.5)+1):
            if num%i==0:
                return False
        return True
    
    answer = 0
    for num in nums:
        if is_prime(num):
            answer += 1

    return answer