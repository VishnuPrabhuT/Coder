# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def equals(n1, n2):
            if not n1 and not n2:
                return True
            if not n1 or not n2:
                return False
            return n1.val == n2.val and equals(n1.left, n2.left) and equals(n1.right, n2.right)
        def traverse(n1, n2):
            return n1 is not None and (equals(n1, n2) or traverse(n1.left, n2) or traverse(n1.right, n2))
        return traverse(s, t)
