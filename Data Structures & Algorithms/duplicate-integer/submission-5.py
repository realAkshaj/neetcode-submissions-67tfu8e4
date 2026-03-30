class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr = sorted(nums)
        for i in range(len(nums)-1):
            if arr[i] == arr[i+1]:
                return True
        return False

