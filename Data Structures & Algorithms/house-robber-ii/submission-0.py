class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def helper(nums):
            memo = {}
            def dfs(i):
                if i >= len(nums):
                    return 0

                if i in memo:
                    return memo[i]

                memo[i] = max(dfs(i + 1), (dfs(i + 2) + nums[i]))
                return memo[i]
            return dfs(0)

        return max(helper(nums[1:]), helper(nums[:len(nums) - 1]))
        
            