class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mn = mx = res = nums[0]
        for x in nums[1:]:
            a = mx * x
            b = mn * x
            mx = max(a, b, x)
            mn = min(a, b, x)
            res = max(res, mx)
        return res