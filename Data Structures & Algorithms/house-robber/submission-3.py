class Solution:
    def houserob(self, ind, nums, n, ans):
        if ind >= n :
            return 0
        if ans[ind] != -1:
            return ans[ind]
        ans[ind] = max(0 + self.houserob(ind + 1, nums, n, ans), nums[ind] + self.houserob(ind + 2, nums, n, ans))
        return ans[ind]

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        ans = [-1] * (n+1)
        return self.houserob(0, nums, n, ans)
        