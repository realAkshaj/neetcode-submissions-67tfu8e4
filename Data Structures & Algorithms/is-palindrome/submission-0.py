class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleaned = re.sub('[^A-Za-z0-9]', '', s)
        s = cleaned.lower()
        left = 0 
        right = len(s) - 1

        while left < right:

            if s[left] == s[right]:
                left += 1
                right -= 1
            
            else:
                return False
        
        return True