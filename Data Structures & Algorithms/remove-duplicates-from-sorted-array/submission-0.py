class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hashmap = {}
        count = 0
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
                count += 1
            
        #print(count)
        #print(hashmap)
        index = 0
        for j in hashmap:
            nums[index] = j
            index += 1

        print(nums[0:count+1])
        return count