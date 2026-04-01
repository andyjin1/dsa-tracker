class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        stack = []
        open_to_close = {'[':']', '{':'}', '(':')'}

        for c in s:
            if c in open_to_close:
                stack.append(c)     
            else:
                if stack:
                    curr = stack.pop()
                    if c != open_to_close[curr]:
                        return False
                else:
                    return False
        
        return False if stack else True

