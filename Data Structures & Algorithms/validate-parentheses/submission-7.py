class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { '}' : '{', ']' : '[', ')' : '('}
        for c in s:
            if stack and c in closeToOpen and closeToOpen[c] == stack[-1]:
                stack.pop()
            elif stack and c in closeToOpen:
                return False
            else:
                stack.append(c)
        return True if not stack else False