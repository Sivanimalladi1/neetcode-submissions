class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for ind, num in enumerate(nums):
            r = target - num 
            if r in hashmap:
                return [hashmap[r], ind]
            else:
                hashmap[num] = ind


        