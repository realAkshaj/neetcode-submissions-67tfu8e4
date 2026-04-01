class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        prefix = [0] * len(nums)
        postfix = [0] * len(nums)

        postfix_curr = prefix_curr = 0

        for i in range(len(nums)):

            prefix_curr += nums[i]
            prefix[i] = prefix_curr
        
        for i in range(len(nums)-1,-1,-1):

            postfix_curr += nums[i]
            postfix[i] = postfix_curr
        
        for i in range(len(nums)):

            if postfix[i] == prefix[i]:
                return i
        
        return -1
        

         