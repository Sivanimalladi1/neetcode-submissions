class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        n = len(nums)
     
        for l in range(n):
            for r in range(l+1, n):
                if nums[l] == nums[r] and abs(l-r) <= k:
                    return True
        
        return False


            
