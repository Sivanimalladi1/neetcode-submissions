class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        n = len(nums)
        cnt = 0
        nums.sort()
        lastele = nums[0]
        ans = []
        
        for i in range(len(nums)):
            if lastele == nums[i]:
                cnt += 1
            else:   
                print("c", cnt, lastele)      
                if cnt > int(n/3):
                    ans.append(lastele)
                    
                cnt = 1
                lastele = nums[i]
                
        if cnt > int(n/3):
            ans.append(lastele)
        
        return ans
        