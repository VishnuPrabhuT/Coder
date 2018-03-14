class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        openB = {'{': '}', '[': ']', '(': ')'}
        closeB = {'}': '{', ']': '[', ')': '('}
        stack = []
        count = 0
        for index, c in enumerate(s):
            if c in openB.keys():
                stack.append(c)
            elif not stack or openB[stack.pop()] != c:
                return False
            count += (c in openB.keys()) - (c in openB.values())
        return count == 0



##########################################################################
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
