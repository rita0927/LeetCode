# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        node = head
        while node:
            next = node.next
            node.next = prev
            prev = node
            node = next 
        return prev 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         pre = None
#         cur = head
#         while cur:
#             next = cur.next
#             cur.next = pre
#             pre = cur
#             cur = next
        
#         return pre 
            