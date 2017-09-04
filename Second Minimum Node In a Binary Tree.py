# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root.left is None and root.right is None:
            return -1
        #return min(self.secMinimum(root.left,[root.val]),self.secMinimum(root.right,[root.val]))
        nodeList=[]
        def secMinimum(node,nodeList):
            if node is None:            
                #print(nodeList) 
                nodeList=sorted(set(nodeList))
            if node:
                nodeList.append(node.val)            
                secMinimum(node.left,nodeList)
                secMinimum(node.right,nodeList)
            #print(nodeList)
        secMinimum(root,nodeList)
        nodeList=set(nodeList)
        if len(nodeList)==1:
            return -1
        return sorted(nodeList)[1]
        
        
        
        
