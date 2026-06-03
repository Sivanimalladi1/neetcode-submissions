import math
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        start = max(weights)
        end = sum(weights)

        while start <= end:
            mid  = int(start+end)//2
            load  = 0
            days_count = 1
            for i in weights:
                if i + load > mid:
                    days_count = days_count + 1
                    load = i
                else:
                    load = load + i

            if days_count <= days:
               
                end = mid - 1
            else:
                start = mid + 1
        return start