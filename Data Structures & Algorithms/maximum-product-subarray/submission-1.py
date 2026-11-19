class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx = mn = res = nums[0]
        for num in nums[1:]:
            a = mx * num
            b = mn * num
            mn = min(num, a, b)
            mx = max(num, a , b)
            res = max(res, mx)
        return res
