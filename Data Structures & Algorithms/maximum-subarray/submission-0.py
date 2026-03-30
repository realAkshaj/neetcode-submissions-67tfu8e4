class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        current = 0
        max_sum = float('-inf')

        for n in nums:

            current = max(current,0)
            current += n

            max_sum = max(current,max_sum)
        
        return max_sum
        