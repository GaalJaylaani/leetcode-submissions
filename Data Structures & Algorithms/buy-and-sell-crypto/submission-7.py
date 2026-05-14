class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minVal = prices[0]
        for p in prices:
            minVal = min(minVal, p)
            maxP = max(maxP, p - minVal)
        return maxP
