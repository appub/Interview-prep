#link -> https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3285/
# maximum subarray solved using kadanes algorithm

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_max = curr_max = nums[0]
        for i in range(1, len(nums)):
            curr_max = max(nums[i], curr_max+nums[i])
            global_max = max(curr_max, global_max)
        return global_max