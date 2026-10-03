class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        minP = prices[0]
        for p in prices:
            minP = min(minP, p)
            best = max(best, p - minP)
        return best