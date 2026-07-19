class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counts = collections.Counter(list(stones))

        answer = 0
        for j in jewels:
            answer += counts[j]
        
        return answer