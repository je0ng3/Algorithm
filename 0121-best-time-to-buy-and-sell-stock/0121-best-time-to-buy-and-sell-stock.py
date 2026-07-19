class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        mini = max(prices)
        for i, price in enumerate(prices):
            mini = min(mini, price)
            mp = max(mp, price-mini)

        return mp