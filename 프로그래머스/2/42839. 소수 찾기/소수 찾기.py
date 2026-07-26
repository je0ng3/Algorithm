def solution(numbers):
    answer = 0
    nums = set()
    visited = [False]*len(numbers)
    def dfs(cur):
        if cur:
            nums.add(int(cur))
        for i, num in enumerate(numbers):
            if not visited[i]:
                visited[i]=True
                dfs(cur+num)
                visited[i]=False
    dfs("")
    def is_prime(num):
        if num<2:
            return False
        for i in range(2, int(num**0.5)+1):
            if num%i==0:
                return False
        return True
    for num in nums:
        if is_prime(num):
            answer +=1
    return answer