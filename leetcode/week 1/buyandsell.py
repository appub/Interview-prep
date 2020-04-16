#link-> https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3287/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0 
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                total += prices[i+1] - prices[i]
        return total