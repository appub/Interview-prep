# in a list with all numbers but ne has a duplicate, find the number that has no duplicates

#link ->https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3283/


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = nums[0]
        for i in range(1, len(nums)):
            ans ^= nums[i]
        return ans