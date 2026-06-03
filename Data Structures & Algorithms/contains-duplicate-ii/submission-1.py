class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        n = len(nums)
        hashmap ={}
        for i in range(n):
            if nums[i] in hashmap and abs(hashmap[nums[i]] -i) <= k:
                    return True
            else:
                hashmap[nums[i]] = i
                
        
        return False


            
