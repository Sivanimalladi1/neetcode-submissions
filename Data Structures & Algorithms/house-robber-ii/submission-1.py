class Solution:
    def houserob(self, start, end, nums, n, ans):
        if start == end:
            return nums[start]

        if start > end:
            return 0

        if ans[start][end] != -1:
            return ans[start][end]

        notpick = 0 + self.houserob(start + 1, end, nums, n, ans)
        pick = nums[start] + self.houserob(start + 2, end, nums, n, ans)

        ans[start][end] = max(pick, notpick)

        return ans[start][end]

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        ans = [[-1 for _ in range(n)] for _ in range(n)]
        if n == 1:
            return nums[0]
        return max(self.houserob(0, n-2, nums, n, ans), self.houserob(1, n-1, nums, n, ans))