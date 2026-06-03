class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        start = max(nums)
        end = sum(nums)
        res = end
        while start <= end:
            mid = int(start+end)//2
            count = 0
            split = 1
            for i in nums:
                if i + count > mid:
                    count = i
                    split += 1
                else:
                    count = i + count

            if split <= k:
                res = mid
                end = mid - 1
            else:
                start = mid + 1    

        return res
