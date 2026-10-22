class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for item in nums:
            if item in seen:
                if seen[item] >= 1:
                    return True
            else:
                seen[item]=1
        return False
