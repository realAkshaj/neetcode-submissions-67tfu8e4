class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        curr = 0
        maxSum = float('-inf')

        for n in nums:

            curr = max(curr,0)
            curr += n

            maxSum = max(maxSum,curr)

        return maxSum
        
        