class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen={}
        for n in nums:
            if n not in seen:
                seen[n]=1
            else:
                seen[n]+=1
        for key, value in seen.items():
            if value == 1:
                return key 
        