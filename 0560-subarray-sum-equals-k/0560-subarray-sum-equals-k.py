class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        answer = 0
        cur = 0

        prefix = {0:1}
        for num in nums:
            cur += num
            if cur-k in prefix:
                answer += prefix[cur-k]
            prefix[cur] = prefix.get(cur, 0)+1

        return answer