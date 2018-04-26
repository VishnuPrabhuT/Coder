# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.res = []
        def getLeaves(root):
            if not root:
                return -1
            l = getLeaves(root.left)
            r = getLeaves(root.right)
            height = 1 + max(l, r)
            if height == len(self.res):
                self.res.append([])
            self.res[height].append(root.val)
            return height
        getLeaves(root)
        return self.res
