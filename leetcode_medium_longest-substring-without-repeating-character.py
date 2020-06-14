# Given a string, find the length of the longest substring without repeating characters.
#Example 1:

#Input: "abcabcbb"
#Output: 3 
#Explanation: The answer is "abc", with the length of 3.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maximum = 0
        for i in range(len(s)):
            char = []
            count = 0
            for c in s[i:]:
                if c not in char:
                    char.append(c)
                    count += 1
                else:
                    break
            if count > maximum:
                maximum = count
        return maximum
