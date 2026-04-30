class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        n = len(nums)
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
                if hashmap[i] > int(n/2):
                    return i
            else:
                hashmap[i] = 1
        