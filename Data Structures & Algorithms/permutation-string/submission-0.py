class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        count = Counter(s1)
        

        left = 0
        right = len(s1) - 1

        while right < len(s2):

            curr = s2[left : right + 1]
            
            if Counter(curr) == count:
                return True
            else:
                left += 1
                right += 1
        
        return False