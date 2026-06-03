class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = 0
        n = len(nums)
        res  = []
        for r in range(0, n - k + 1):
            a = []
            for i in range(r, r + k):
                a.append(nums[i])
            res.append(max(a))
        return res

