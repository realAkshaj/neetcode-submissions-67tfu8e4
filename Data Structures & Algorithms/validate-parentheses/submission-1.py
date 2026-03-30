class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: 
            return False
        stack = []
        mpp = {')':'(' , '}':'{' , ']':'[' }
        for char in s:
            if char in mpp:
                if stack and stack[-1] == mpp[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return not stack

        