class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        nums = [i for i in range(1, n+1)]

        def dfs(idx, cur):
            if len(cur)==k:
                answer.append(cur[:])
                return
            if idx>=len(nums):
                return 

            cur.append(nums[idx])
            dfs(idx+1, cur)
            cur.pop()
            dfs(idx+1, cur)
            
        dfs(0, [])

        return answer