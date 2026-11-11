class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo={}

        def f(i):
            if i < 0:
                return 0
            if i<=1:
                return cost[i]
            if i not in memo:
                memo[i]=cost[i] + min(f(i-1),f(i-2))
            return memo[i]
        
        n = len(cost)
        return min(f(n-1),f(n-2))