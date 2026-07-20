class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            '2':'abc', '3':'def','4':'ghi','5':'jkl',
            '6':'mno','7':'pqrs', '8':'tuv', '9':'wxyz'
        }

        answer = []
        def dfs(idx, cur):
            if len(cur)==len(digits):
                answer.append(cur)
                return
            for i in range(idx, len(digits)):
                for c in dic[digits[i]]:
                    cur+=c
                    dfs(i+1, cur)
                    cur=cur[:-1]


        dfs(0, '')
        return answer