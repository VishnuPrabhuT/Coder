# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        copy = collections.defaultdict(lambda: RandomListNode(0))
        node = head
        copy[None] = None
        while node:
            copy[node].label = node.label
            copy[node].next = copy[node.next]
            copy[node].random = copy[node.random]
            node = node.next
        return copy[head]
