# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        count, curr = 0, head
        while curr and count != k:
            count += 1
            curr = curr.next
        if count == k:
            curr = self.reverseKGroup(curr, k)
            while count > 0:
                count -= 1
                temp = head.next
                head.next = curr
                curr = head
                head = temp
            head = curr
        return head
