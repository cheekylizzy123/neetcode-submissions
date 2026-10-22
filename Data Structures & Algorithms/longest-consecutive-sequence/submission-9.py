class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        best = 0
        for n in s:
            if n - 1 not in s:            # n is the START of a run
                length = 1
                while n + length in s:    # walk forward through the run
                    length += 1
                best = max(best, length)
        return best









                