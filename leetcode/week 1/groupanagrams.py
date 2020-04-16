#link to question -> https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3288/
# grouping anagrams together

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = dict()
        for ele in strs:
            ana = "".join(sorted(ele))
            if ana in ans:
                ans[ana].append(ele)
            else:
                ans[ana] = [ele]
        return ans.values()