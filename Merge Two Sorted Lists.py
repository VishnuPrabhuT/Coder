# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head=ListNode(0)
        curr=head
        if not l1:
            return l2
        elif not l2:
            return l1
        res=[]
        while l1 and l2:
            #print(curr.val)            
            if l1.val<l2.val:                
                curr.next=l1
                #res.append(curr.val)
                l1=l1.next
            else:
                curr.next=l2
                #res.append(curr.val)
                l2=l2.next
            curr=curr.next
        curr.next=l1 or l2
        return head.next
            
