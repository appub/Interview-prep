#link -> https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3289/

from collections import Counter
class Solution:
    def countElements(self, arr: List[int]) -> int:
        cntr = Counter(arr)
        ans = 0
        for ele in cntr:
            if ele + 1 in cntr:
                ans += cntr[ele]
        return ans