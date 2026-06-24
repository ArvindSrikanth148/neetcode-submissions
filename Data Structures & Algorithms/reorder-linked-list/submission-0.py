# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head:
            slow, fast=head, head.next 

            while fast and fast.next:
                slow=slow.next
                fast=fast.next.next

            second=slow.next
            prev=None 
            slow.next=None
            while second:

                temp=second.next
                second.next=prev
                prev=second 
                second = temp
            h=head
            while prev:
                temp=h.next 
                temp2=prev.next 
                h.next=prev
                prev.next=temp
                h=temp
                prev=temp2
            

            
        

        
        
 