class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        window = set()
        maxLen = 0
        l = 0
        r = 0

        while r < len(s):

            if s[r] in window:
                window.remove(s[l])
                l += 1
            else:
                window.add(s[r])
                maxLen = max(maxLen, r - l + 1)
                r += 1
        
        return maxLen