# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.pre = None
        def isBST(root):
            if not root:
                return True
            if not isBST(root.left):
                return False
            if self.pre and self.pre.val >= root.val:
                return False
            self.pre = root
            return isBST(root.right)
        return isBST(root)

#####################################################################################################
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isBST(root, left, right):
            if not root:
                return True
            print(left, root.val, right)
            if root.val <= left or root.val >= right:
                return False
            return isBST(root.left, left, root.val) and isBST(root.right, root.val, right)
        return isBST(root, -sys.maxsize, sys.maxsize)
