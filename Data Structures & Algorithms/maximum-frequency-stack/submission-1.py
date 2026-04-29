class FreqStack:

    def __init__(self):
        self.listofstacks = defaultdict(list)
        self.maxCount = 0
        self.valFreq = {}

    def push(self, val: int) -> None:
        
        self.valFreq[val] = self.valFreq.get(val,0) + 1
        self.listofstacks[self.valFreq[val]].append(val)
        self.maxCount = max(self.maxCount,self.valFreq[val])
        

    def pop(self) -> int:

        stack = self.listofstacks[self.maxCount]
        val = stack.pop()
        if len(stack) == 0:
            self.maxCount -= 1
        self.valFreq[val] -= 1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()