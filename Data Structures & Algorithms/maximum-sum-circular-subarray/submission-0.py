class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        globMax, globMin = float('-inf'),float('inf')
        curMin,curMax = 0 , 0
        total = 0

        for n in nums:

            curMax = max(curMax + n, n)
            curMin = min(curMin + n, n)

            total += n
            globMax = max(globMax,curMax)
            globMin = min(globMin,curMin)

        
        if globMax > 0:        
            return max(globMax, total - globMin)
        return globMax

        
            

        
