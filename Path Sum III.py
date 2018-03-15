# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        def findWays(root, sum):
            if not root:
                return 0
            return int(root.val == sum) + findWays(root.left, sum - root.val) + findWays(root.right, sum - root.val)
        return findWays(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
