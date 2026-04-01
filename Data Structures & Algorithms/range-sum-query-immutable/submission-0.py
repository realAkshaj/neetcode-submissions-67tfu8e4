class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        self.total = 0
        for n in nums:
            self.total += n
            self.prefix.append(self.total)
        
    def sumRange(self, left: int, right: int) -> int:
        
        sumLeft = self.prefix[left - 1] if left > 0 else 0
        sumRight = self.prefix[right]

        return sumRight - sumLeft


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)