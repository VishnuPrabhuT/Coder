class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        close={'}':'{',')':'(',']':'['}
        stack=[] 
        for c in s:
            if c in close.values():
                stack.append(c)
            elif c in close.keys():
                if stack==[] or close[c]!=stack.pop():
                    return False
        return stack==[]
