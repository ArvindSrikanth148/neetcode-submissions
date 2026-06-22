# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

       
        if list1!=None and list2!=None :
            if list1.val> list2.val:
                head=list2
                tail=list1
            else:
                head=list1
                tail=list2  
            ret=head
            
            while head!=None and tail!=None:
                if head.next !=None :
                    if head.next.val>tail.val:
                        t1=tail.next
                        temp=tail
                        temp.next=head.next
                        print(temp.next.val)
                        head.next=temp
                        tail=t1
                        
                        
                else :
                    head.next=tail
                    break

                head=head.next 
        


                
            if head!=None and tail != None:
                head.next=tail
        

            return ret
        elif list1==None:
            return list2
        else :
            return list1
                
                

      


        



        

            
