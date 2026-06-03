class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        ans = [0] * n
        for i in range(n):
            j = (i + k) % n
            ans[j] = nums[i]
        nums[:] = ans
        print(nums)
        