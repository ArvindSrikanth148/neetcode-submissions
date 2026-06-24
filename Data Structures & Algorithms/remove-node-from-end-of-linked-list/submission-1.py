# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next==None:
            return None
        
        i=0
        right=head
        while i<n:
            right=right.next
            i=i+1
        if right==None:
            return head.next  
        left=head

        while right:
            prev=left
            left=left.next
            right=right.next

        prev.next=left.next
        return head
        

        
            



    