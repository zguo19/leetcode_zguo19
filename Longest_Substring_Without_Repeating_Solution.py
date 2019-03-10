#3. Longest Substring Without Repeating Characters (Medium)
#Given a string, find the length of the longest substring without repeating characters.
#Example 1:
#Input: "abcabcbb"
#Output: 3 
#Explanation: The answer is "abc", with the length of 3. 
#Example 2:
#Input: "bbbbb"
#Output: 1
#Explanation: The answer is "b", with the length of 1.
#Example 3:
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
    #  Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = 0
        ma = 0
        lst = ""
        while(s):
            if s[0] in lst:
                s = lst[1:] + s
                n = 0
                lst = ""
            else:
                n += 1
                if n > ma:
                    ma = n
                lst = lst + s[0]
                s = s[1:]
        return ma