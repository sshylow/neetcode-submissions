class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {
            '(' :')', 
            '{': '}', 
            '[' : ']'
        }
        for char in s:
            if char in "{[(": # append open brackets first
                stack.append(char)
            else: 
                if not stack or char != matches[stack[-1]]: #nothing in the stack or the first item in the stack doesn't match the closing bracket
                    return False
                stack.pop() #match found onto the next bracket

        return not stack