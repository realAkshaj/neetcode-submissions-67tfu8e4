class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_area = 0 
        left = 0
        right = len(heights) - 1

        while left < right:

            width = right - left
            height = min(heights[right],heights[left])

            curr_area = width * height
            max_area = max(curr_area,max_area)

            if heights[left] > heights[right]:
                right -= 1            
            else:
                left += 1
        
        return max_area



        