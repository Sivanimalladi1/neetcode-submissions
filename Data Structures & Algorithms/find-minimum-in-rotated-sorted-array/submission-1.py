class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        minval = float('inf')
        while start <= end:
            mid = int(start+end)//2
            if nums[start] <= nums[mid]:
                minval = min(minval, nums[start])
                start = mid + 1
            else:
                minval = min(minval, nums[mid])
                end = mid - 1
        return minval
        