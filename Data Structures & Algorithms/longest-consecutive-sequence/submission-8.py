class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        nums = sorted(set(nums))   # removes duplicates and sorts ascending

        max_lg = 1      # longest run seen so far
        streak = 1     # length of the current run 

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                streak += 1                    # run continues
                max_lg = max(max_lg, streak)   # update best as the run grows
            else:
                streak = 1                     # run broke, start a new one

        return max_lg









                