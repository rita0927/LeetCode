# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if left == right:
            return head 
        
        dummy = prev = ListNode(0, head)
        i = 1
        
        while i < left:
            prev = prev.next 
            i += 1
        
        cur = prev.next 
        next = cur.next 
        
        while i < right:
            temp = next.next 
            next.next = cur
            cur = next 
            next = temp
            i += 1
        
        prev.next.next = next 
        prev.next = cur 
        
        return dummy.next 
        

        