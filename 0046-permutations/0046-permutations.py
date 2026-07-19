class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []        

        n = len(nums)
        visited = [False]*n
        def dfs(cur):
            if len(cur)==n:
                answer.append(cur[:])
                return
            for i in range(n):
                if not visited[i]:
                    visited[i] = True
                    cur.append(nums[i])
                    dfs(cur)
                    cur.pop()
                    visited[i] = False

        dfs([])
        return answer