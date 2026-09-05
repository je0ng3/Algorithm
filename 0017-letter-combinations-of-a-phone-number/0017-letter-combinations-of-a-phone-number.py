from collections import deque

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            '2':'abc', '3':'def','4':'ghi','5':'jkl',
            '6':'mno','7':'pqrs', '8':'tuv', '9':'wxyz'
        }

        q = deque(list(dic[digits[0]]))
        for digit in digits[1:]:
            for _ in range(len(q)):
                tmp = q.popleft()
                for c in dic[digit]:
                    q.append(tmp+c)
        return list(q)