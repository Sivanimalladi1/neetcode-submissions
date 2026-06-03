class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        n = len(nums)
        minlen = float('inf')
        sums = 0
        for r in range(n):
            sums += nums[r]
            while sums  >= target:
                minlen = min(minlen, r - l + 1)
                sums -= nums[l]
                l += 1
                

        return 0 if minlen == float('inf') else minlen