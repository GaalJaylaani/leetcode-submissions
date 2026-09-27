class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            d[num] = d.get(num, 0) + 1
        for n,c in d.items():
            freq[c].append(n)
        res = []
        for j in range(len(freq) - 1, 0 , -1):
            for n in freq[j]:
                res.append(n)
                if len(res) == k:
                    return res

        