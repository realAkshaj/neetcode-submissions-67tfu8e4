class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mpp = {}
        for index,value in enumerate(nums):
            diff = target - value
            if diff in mpp:
                return [mpp[diff],index]
            mpp[value] = index
        