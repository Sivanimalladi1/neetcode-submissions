class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        i = 0
        j = n-1
        
        while i< j:
            if nums[i] + nums[j] == target:
                return sorted([i,j])
            elif nums[i] + nums[j] > target:
                j -= 1
            else:
                i += 1
        return []


        