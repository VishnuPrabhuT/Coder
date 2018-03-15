# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        ans = False
        if not root:
            return False
        if not root.left and not root.right and sum == root.val:
            return True
        sum -= root.val
        ans |= self.hasPathSum(root.left, sum)
        ans |= self.hasPathSum(root.right, sum)
        return ans
