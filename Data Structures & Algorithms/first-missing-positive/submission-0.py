class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
    
        hashmap = set(nums)

        res = 1
        while res in hashmap:
            res += 1
        
        return res