class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        len1 = len(word1)
        len2 = len(word2)
        length = min(len1,len2)
        res = ""

        for i in range(length):

            res += word1[i] + word2[i]
        
        if len1 > len2:

            res += word1[length:]
        
        elif len2 > len1:

            res += word2[length:]
        
        return res






