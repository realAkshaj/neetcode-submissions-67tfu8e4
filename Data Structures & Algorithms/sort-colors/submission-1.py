class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        number_of_colors = [0] * 3

        for num in nums:
            number_of_colors[num] += 1
        
        index = 0
        for i in range(3):
            while number_of_colors[i] > 0:
                 number_of_colors[i] -= 1
                 nums[index] = i
                 index += 1
        