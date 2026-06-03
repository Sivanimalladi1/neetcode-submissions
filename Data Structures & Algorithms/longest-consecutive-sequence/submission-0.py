class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        last_small = float('-inf')
        length = 0
        maxlen = 0
        for i in range(len(nums)):
            if nums[i] -1 == last_small:
               
                last_small = nums[i]
                length += 1
            elif(nums[i] != last_small):
                
                length = 1
                last_small = nums[i]
            maxlen = max(maxlen, length)
        return maxlen



