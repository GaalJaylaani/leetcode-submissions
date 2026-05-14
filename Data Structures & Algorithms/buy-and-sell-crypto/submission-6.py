class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minVal = float('inf')
        for p in prices:
            minVal = min(minVal, p)
            maxP = max(maxP, p - minVal)
        return maxP
