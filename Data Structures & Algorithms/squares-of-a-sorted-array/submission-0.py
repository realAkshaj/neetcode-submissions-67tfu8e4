class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        res = [0] * n
        index = n - 1
        left = 0
        right = n - 1

        while left <= right:

            left_val = abs(nums[left])
            right_val = abs(nums[right])

            if left_val >= right_val:

                res[index] = left_val ** 2
                left += 1
                index -= 1
            
            else:

                res[index] = right_val ** 2
                right -= 1
                index -= 1
        
        return res