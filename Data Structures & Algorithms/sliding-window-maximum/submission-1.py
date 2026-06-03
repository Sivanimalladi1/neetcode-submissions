class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = k 
        n = len(nums)
        res  = []
        while r <= n:
            #print("l, r", l, r)
            res.append(max(nums[l:r]))
            r = r + 1
            l = l + 1

        return res

