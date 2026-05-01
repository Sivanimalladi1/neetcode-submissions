class Solution:
    def merge(self, start, mid, end, nums):
        temp = []
        left = start
        right = mid + 1
        while(left<= mid and right<=end):
            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left += 1
            else:
                temp.append(nums[right])
                right += 1

        while(left<=mid):
            temp.append(nums[left])
            left += 1
        while(right<=end):
            temp.append(nums[right])
            right += 1
        for i in range(start, end+1):
            nums[i] = temp[i-start]
        
    def mergeSort(self, start, end, nums):
        if start >= end:
            return 
        mid =  int(start + (end- start)/2)
        self.mergeSort(start, mid, nums)
        self.mergeSort(mid+1, end, nums)
        self.merge(start, mid, end, nums)

    def sortArray(self, nums: List[int]) -> List[int]:
        start = 0
        end = len(nums) - 1
        self.mergeSort(start, end, nums)
        return nums
        

        