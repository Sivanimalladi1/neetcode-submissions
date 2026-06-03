class Solution:
    def climbcost(self,  ind, n, cost, res):
        if ind >= n:
            return 0
        if res[ind] != -1:
            return res[ind]

        res[ind] = cost[ind] + min(self.climbcost(ind+1, n, cost, res), self.climbcost(ind+2, n, cost, res))
        return res[ind]
        
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        res = [-1] * (n+1)
        return min(self.climbcost(0, n, cost, res), self.climbcost(1, n, cost, res))