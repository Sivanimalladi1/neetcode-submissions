import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        
        minval = float('inf')
        while start <= end:
            mid = int(start+(end-start)/2)
            count = 0
            for i in piles:
                count = math.ceil(i/mid) + count
            if count <= h:
                minval = min(minval, mid)
                end = mid - 1
            else:
                start = mid + 1
        return minval
