#link-> https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3286/
# move zeroes to end inplace
class Solution:

    def moveZeroes(self, nums):
        zero = 0  # records the position of "0"
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
