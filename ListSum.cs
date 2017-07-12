/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    
   
    
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        ListNode sumList=new ListNode(0);
        ListNode head=sumList;
        int carry=0;
        int rem=0;        
                
                while (l1 != null || l2 != null || carry!=0 ){                    
                    ListNode curr=new ListNode(0);
                    int sum=l2==null ? 0:l2.val;
                    sum+=l1==null ? 0:l1.val;
                    sum+=carry;
                    curr.val=(sum)%10;
                    carry=(sum)/10;                                        
                    sumList.next=curr;
                    sumList=curr;
                    l1=l1==null?l1:l1.next;
                    l2=l2==null?l2:l2.next;
                }
                return head.next;
                
             
             
    }
}
