class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        i = 0
        j = n-1
        target = abs(target)
        while i< j:
            if abs(nums[i] + nums[j]) == target:
                return sorted([i,j])
            elif abs(nums[i] + nums[j]) > target:
                j -= 1
            else:
                i += 1
        return []


        