class Solution:
    def isValid(self, s: str) -> bool:
        

        stack = []
        mpp = {')':'(', ']':'[', '}':'{'}

        for bracket in s:
            if bracket in mpp:
                if stack and stack[-1] == mpp[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        
        return len(stack) == 0
        