class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)<=1 or len(s)%2==1:
            return False
        stack = []
        strdict = {')':'(', '}':'{', ']':'['}
        
        for i in s:
            if i in strdict:
                if stack and stack[-1] == strdict[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        if stack:
            return False
        return True