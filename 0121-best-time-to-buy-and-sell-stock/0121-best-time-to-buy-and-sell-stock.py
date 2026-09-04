class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        mini = prices[0]
        for price in prices[1:]:
            if mini<price:
                answer = max(answer, price-mini)
            else:
                mini = price
        return answer