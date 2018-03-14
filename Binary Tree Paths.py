# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res, path = [], ""
        if not root:
            return []
        def paths(res, path, current):
            if not current.left and not current.right:
                res.append(path + str(current.val))
            if current.left:
                paths(res, path + str(current.val) + "->", current.left)
            if current.right:
                paths(res, path + str(current.val) + "->", current.right)
        paths(res, path, root)
        return res
