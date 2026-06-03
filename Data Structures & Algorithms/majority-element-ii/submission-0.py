class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        n = len(nums)
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
               
            else:
                hashmap[i] = 1
        ans = []
        for val, c in hashmap.items():
            if c > int(n/3):
                ans.append(val)
        
        return ans
        