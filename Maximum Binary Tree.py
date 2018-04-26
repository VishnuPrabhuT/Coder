# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return
        root = TreeNode(max(nums))
        ind = nums.index(root.val)
        root.left = self.constructMaximumBinaryTree(nums[:ind])
        root.right = self.constructMaximumBinaryTree(nums[ind+1:])
        return root
