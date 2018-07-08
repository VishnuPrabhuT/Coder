# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q = [root]
        flag = 1
        res = []
        while q:
            level = []
            for n in q:
                level.append(n.val)
            res.append(level[::flag])
            temp = []
            for n in q:
                if n.left:
                    temp.append(n.left)
                if n.right:
                    temp.append(n.right)
                print(n.val)
            flag *= -1
            q = temp
        return res
            
