class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        result = []
        def best(remaining):
            if remaining in memo:
                return memo[remaining]
            if remaining == 0:
                return 1
            if remaining < 0:
                return 0
            left = best(remaining - 1)
            right = best(remaining - 2)
            result = left + right
            memo[remaining] = result
            return result
        return best(n)
