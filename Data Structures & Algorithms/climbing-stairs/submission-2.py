class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        result = []
        def ways(remaining):
            if remaining in memo:
                return memo[remaining]
            if remaining == 0:
                return 1
            if remaining < 0:
                return 0
            left = ways(remaining - 1)
            right = ways(remaining - 2)
            result = left + right
            memo[remaining] = result
            return result
        return ways(n)
