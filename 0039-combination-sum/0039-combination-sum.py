class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        def dfs(cur, idx, s):
            if s==target:
                answer.append(cur[:])
                return
            
            for i in range(idx, len(candidates)):
                c = candidates[i]
                if s+c<=target:
                    dfs(cur+[c], i, s+c)
        
        dfs([], 0, 0)
        return answer