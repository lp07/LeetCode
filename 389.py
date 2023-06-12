# 389. Find the Difference
# You are given two strings s and t.
# String t is generated by random shuffling string s and then add one more letter at a random position.
# Return the letter that was added to t.
# Example 1:
# Input: s = "abcd", t = "abcde", Output: "e"
# Explanation: 'e' is the letter that was added.
# Example 2:
# Input: s = "", t = "y", Output: "y"

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in t:
            if s.count(i) != t.count(i):
                return i
solution = Solution()
result = solution.findTheDifference(s="abcd", t="abcde")
print(result)

# output: e