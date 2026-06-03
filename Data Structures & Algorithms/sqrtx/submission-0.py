class Solution:
    def mySqrt(self, x: int) -> int:
        start = 1
        end = x
        while start <= end:
            mid = int(start+end)//2
            val = mid * mid
            if val <= x:
                start = mid + 1
            else:
                end = mid -1
        return end
        