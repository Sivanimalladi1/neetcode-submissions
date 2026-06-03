class Solution:
    def stepdcount(self, n, res):
        if n == 0 or n==1:
            return 1
        if res[n] != -1:
            return res[n]
        left = self.stepdcount(n-1, res)
        res[n] = left
        right = self.stepdcount(n-2, res)
        res[n] += right
        return left + right

    def climbStairs(self, n: int) -> int:
        res = [-1] * (n+1)
        return self.stepdcount(n, res)
        #print(res)