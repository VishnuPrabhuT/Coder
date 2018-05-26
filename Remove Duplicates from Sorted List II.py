# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = prev = ListNode(0)
        anchor = head
        dummy.next = anchor
        prev.next = anchor
        while anchor and anchor.next:
            if anchor.val == anchor.next.val:
                while anchor and anchor.next and anchor.val == anchor.next.val:
                    anchor = anchor.next
                anchor = anchor.next
                prev.next = anchor
            else:   
                prev = prev.next
                anchor = anchor.next
        return dummy.next
