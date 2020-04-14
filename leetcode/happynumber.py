# link -> https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3284/
#similar to cycle detection algo

class Solution:
    def isHappy(self, n: int) -> bool:
        mem = set()
        while n not in mem:
            mem.add(n)
            ans = sum(int(x)**2 for x in str(n))
            if ans == 1:
                return True
            n = ans
        return False