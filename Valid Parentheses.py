# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        def checkSym(left, right):
            if not left and not right:
                return True
            elif not left or not right:
                return False
            if left.val == right.val:
                l = checkSym(left.left, right.right)
                r = checkSym(left.right, right.left)
            else:
                return False
            return l and r
        return checkSym(root.left, root.right)

#########################################################################
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
