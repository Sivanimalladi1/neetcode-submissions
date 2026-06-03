class Solution:
    def tNumber(self, n, res):
        if n == 2 or n == 1 :
            return 1
        if n == 0:
            return 0
        if res[n] != -1:
            return res[n]
        res[n] = self.tNumber(n-1, res) + self.tNumber(n-2, res) + self.tNumber(n-3, res)
        return res[n]

    def tribonacci(self, n: int) -> int:
        res = [-1] * (n+1)
        return self.tNumber(n, res)