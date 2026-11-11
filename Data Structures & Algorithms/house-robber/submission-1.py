class Solution:
    def rob(self, nums: List[int]) -> int:
        memo={}

        def f(i):
            if i<0:
                return 0 
            if i not in memo:
                memo[i]= max(f(i-1), nums[i]+f(i-2))
            return memo[i]
        
        n = len(nums)-1
        return f(n)
        