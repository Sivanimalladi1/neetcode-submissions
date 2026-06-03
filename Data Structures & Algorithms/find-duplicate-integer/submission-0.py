class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashmap ={}
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
                if hashmap[i] > 1:
                    
                    return i
            else:
                hashmap[i] = 1

        print(hashmap)