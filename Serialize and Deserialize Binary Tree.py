# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def serHelper(root):
            if root:
                ret.append(str(root.val))
                serHelper(root.left)
                serHelper(root.right)
            else:
                ret.append("#")
        ret = []
        serHelper(root)
        return ' '.join(ret)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def deserHelper():
            val = next(ret)
            if val == '#':
                return None
            root = TreeNode(int(val))
            root.left = deserHelper()
            root.right = deserHelper()
            return root
        ret = iter(data.split())
        return deserHelper()
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
