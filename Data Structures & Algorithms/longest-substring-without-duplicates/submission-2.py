class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        window = set()

        left = curr = 0
        maxLen = 0

        for right in range(len(s)):
            
            while s[right] in window:

                window.remove(s[left])
                left += 1
                curr -= 1
            
            window.add(s[right])            
            curr += 1
            maxLen = max(curr,maxLen)
        
        return maxLen
            


























        
        # window = set()
        # maxLen = 0
        # left = 0
        # curr = 0

        # for right in range(len(s)):
            
        #     curr += 1

        #     while s[right] in window:
        #         window.remove(s[left])
        #         left += 1
        #         curr -= 1
            
        #     window.add(s[right])
            
        #     maxLen = max(maxLen,curr)

        # return maxLen
            

