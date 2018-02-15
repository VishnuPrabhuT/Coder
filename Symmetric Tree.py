# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mirror(self,left,right):
        if left is None and right is None:
            return True
        if left and right:
            if left.val==right.val:
                return self.mirror(left.left,right.right) and self.mirror(left.right,right.left)
        return False
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if root:            
            return root.val==root.val and self.mirror(root.left,root.right) and self.mirror(root.right,root.left)
        else:
            return False
        
########################################################################################################################################
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
        if root:
            return True and self.isMirror(root.left, root.right)
        else:
            return True
    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left and right:
            print(left.val, right.val)
            return left.val == right.val and self.isMirror(left.left,right.right) and self.isMirror(left.right,right.left)
