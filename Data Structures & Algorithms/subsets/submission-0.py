class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums = list(nums)
        results = []
        path = []
        def backtrack(i):
            if i == len(nums):
                results.append(path[:])
                return
            path.append(nums[i])
            backtrack(i + 1)
            path.pop()
            backtrack(i + 1)
            return
        backtrack(0)
        return results