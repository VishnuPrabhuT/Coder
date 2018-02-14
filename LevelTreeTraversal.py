# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        depth = [root]
        res = []
        while root and depth:
            res.append([node.val for node in depth]) 
            temp = []
            for node in depth:
                temp.extend([node.left, node.right])
            depth = [node for node in temp if node]
        return res
