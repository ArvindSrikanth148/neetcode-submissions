# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head=ListNode()
        h=head
        carry=0
        while l1 and l2:
            
            cur=carry+l1.val+l2.val 
            carry=cur//10
            value=cur-carry*10

            h.val=value 
            l1=l1.next
            l2=l2.next
            if l1 and l2:
                t=ListNode()
                h.next=t
                h=h.next
        if l1: 
            while l1:
                cur=carry+l1.val 
                carry=cur//10
                value=cur-carry*10
                t=ListNode()
                h.next=t
                h=h.next
                h.val=value
                l1=l1.next
        elif l2: 
            while l2:
                cur=carry+l2.val 
                carry=cur//10
                value=cur-carry*10
                t=ListNode()
                h.next=t
                h=h.next
                h.val=value
                l2=l2.next

        if carry!=0:
            t=ListNode()
            h.next=t
            h=h.next
            h.val=carry
        return head

                

        